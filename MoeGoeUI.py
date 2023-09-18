import os
from pathlib import Path
from PySide6.QtWidgets import (QApplication, QMainWindow, QFileDialog, QMessageBox, QListWidgetItem)
from PySide6.QtCore import Qt
from openpyxl.reader.excel import load_workbook

from ui_main import Ui_MainWindow
from MoeGoe import load_model, model_tts


class Window(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.model_path = ''
        self.config_path = ''
        self.length = 1
        self.noise = 0.6
        self.noise_w = 0.8
        self.speaker_id = 0
        self.speaker_name = ''
        self.search_name = ''
        self.search_index = -1
        self.speakers = []
        self.text_input = ''
        self.save_path = ''
        self.xl_path = ''
        self.xl_lines_header = '台词'
        self.xl_filename_header = '文件名'
        self.xl_lang_header = '语言'
        self.lang_list = ['', 'ZH', 'JA', 'EN']
        self.lang = ''
        self.model_loaded = False
        self.init_ui_data()
        self.create_connections()

    def init_ui_data(self):
        self.edit_model.setText(self.model_path)
        self.edit_config.setText(self.config_path)
        self.spin_length.setValue(self.length)
        self.spin_noise.setValue(self.noise)
        self.spin_noise_w.setValue(self.noise_w)
        self.edit_speaker.setText(self.speaker_name)
        self.update_speaker_list()
        self.edit_text_input.setText(self.text_input)
        self.edit_save_path.setText(self.save_path)
        self.edit_xl.setText(self.xl_path)
        self.edit_lines_header.setText(self.xl_lines_header)
        self.edit_filename_header.setText(self.xl_filename_header)
        self.edit_lang_header.setText(self.xl_lang_header)
        self.comb_lang.clear()
        self.comb_lang.addItems(self.lang_list)

    def create_connections(self):
        self.btn_load_model.clicked.connect(self.btn_load_model_clicked)
        self.btn_load_config.clicked.connect(self.btn_load_config_clicked)
        self.edit_model.textChanged.connect(self.edit_model_text_changed)
        self.edit_config.textChanged.connect(self.edit_config_text_changed)
        self.spin_length.textChanged.connect(self.spin_length_text_changed)
        self.spin_noise.textChanged.connect(self.spin_noise_text_changed)
        self.spin_noise_w.textChanged.connect(self.spin_noise_w_text_changed)
        self.edit_speaker.textChanged.connect(self.edit_speaker_text_changed)
        self.btn_search_pre.clicked.connect(self.btn_search_clicked)
        self.btn_search_next.clicked.connect(self.btn_search_clicked)
        self.list_widget_speaker.itemClicked.connect(self.list_widget_speaker_item_clicked)
        self.edit_text_input.textChanged.connect(self.edit_text_input_text_changed)
        self.edit_save_path.textChanged.connect(self.edit_save_path_text_changed)
        self.btn_save.clicked.connect(self.btn_save_clicked)
        self.btn_play.clicked.connect(self.btn_play_clicked)
        self.btn_load_xl.clicked.connect(self.btn_load_xl_clicked)
        self.edit_xl.textChanged.connect(self.edit_xl_text_changed)
        self.edit_lines_header.textChanged.connect(self.edit_lines_header_text_changed)
        self.edit_filename_header.textChanged.connect(self.edit_filename_header_text_changed)
        self.edit_lang_header.textChanged.connect(self.edit_lang_header_text_changed)
        self.btn_xl_save.clicked.connect(self.btn_xl_save_clicked)
        self.comb_lang.textActivated.connect(self.comb_lang_text_activated)

    def try_load_model(self):
        if Path(self.model_path).is_file() and Path(self.config_path).is_file():
            try:
                (self.speakers, self.n_symbols, self.emotion_embedding,
                 self.hps_ms, self.net_g_ms) = load_model(self.model_path, self.config_path)

                self.model_loaded = True
                self.speaker_id = 0
                self.update_speaker_list()
                self.statusbar.showMessage('模型已加载。')
            except Exception as e:
                print(f'模型加载失败！\n{e}')

    def tts_from_list(self, text_list):
        if self.n_symbols != 0:
            if not self.emotion_embedding:
                for text, filename, lang in text_list:  # type:str,str
                    if not filename.endswith('.wav'):
                        filename += '.wav'
                    if lang:
                        text = f'[{lang}]{text}[{lang}]'
                    model_tts(self.speaker_id, text, filename, self.hps_ms, self.net_g_ms)
                    self.statusbar.showMessage(f'Successfully saved! - {filename}')
            else:
                QMessageBox.warning(self, '警告', '合成失败\nemotion_embedding...')
        else:
            QMessageBox.warning(self, '警告', '合成失败\nn_symbols == 0')

    def update_speaker_list(self):
        self.list_widget_speaker.clear()
        self.list_widget_speaker.addItems(self.speakers)
        self.list_widget_speaker.setCurrentRow(self.speaker_id)

    def btn_load_model_clicked(self):
        filename, _ = QFileDialog.getOpenFileName(self, '打开模型', filter='模型文件(*.pth)')
        if not filename: return
        self.model_path = filename
        self.edit_model.setText(filename)
        self.try_load_model()

    def btn_load_config_clicked(self):
        filename, _ = QFileDialog.getOpenFileName(self, '打开配置', filter='配置文件(*.json)')
        if not filename: return
        self.config_path = filename
        self.edit_config.setText(filename)
        self.try_load_model()

    def edit_model_text_changed(self, text):
        self.model_path = text.strip()

    def edit_config_text_changed(self, text):
        self.config_path = text.strip()

    def spin_length_text_changed(self, text):
        self.length = float(text)

    def spin_noise_text_changed(self, text):
        self.noise = float(text)

    def spin_noise_w_text_changed(self, text):
        self.noise_w = float(text)

    def edit_speaker_text_changed(self, text):
        self.search_name = text.strip()

    def btn_search_clicked(self):
        if not self.search_name:
            return
        items = self.list_widget_speaker.findItems(self.search_name, Qt.MatchFlag.MatchContains)
        if not items: return
        if self.sender() == self.btn_search_pre:
            self.search_index -= 1
        if self.sender() == self.btn_search_next:
            self.search_index += 1
        if self.search_index >= len(items):
            self.search_index = 0
        if self.search_index < 0:
            self.search_index = len(items) - 1
        item = items[self.search_index]
        self.list_widget_speaker.setCurrentItem(item)
        text = item.text()
        row = self.list_widget_speaker.row(item)

        self.speaker_id = row
        self.speaker_name = text
        print(self.speaker_id, self.speaker_name)

    def list_widget_speaker_item_clicked(self, item: QListWidgetItem):
        self.speaker_id = self.list_widget_speaker.row(item)
        self.speaker_name = item.text()

    def edit_text_input_text_changed(self):
        self.text_input = self.edit_text_input.toPlainText().strip()

    def edit_save_path_text_changed(self, text):
        self.save_path = text.strip()

    def btn_save_clicked(self):
        if not self.model_loaded:
            QMessageBox.warning(self, '警告', '模型未加载！')
            return
        if not self.text_input or not self.save_path:
            QMessageBox.warning(self, '警告', '文本和保存路径不能为空！')
            return
        text_list = [[self.text_input, self.save_path, self.lang]]
        self.tts_from_list(text_list)
        QMessageBox.information(self, '信息', '成功生成语音！')

    def btn_play_clicked(self):
        if not self.save_path: return
        filename = self.save_path
        if not filename.endswith('.wav'):
            filename += '.wav'
        if not Path(filename).is_file():
            return

        os.startfile(filename)

    def btn_load_xl_clicked(self):
        filename, _ = QFileDialog.getOpenFileName(self, '打开Excel', filter='Excel文件(*.xlsx)')
        if not filename: return
        self.xl_path = filename
        self.edit_xl.setText(filename)

    def edit_xl_text_changed(self, text):
        self.xl_path = text.strip()

    def edit_lines_header_text_changed(self, text):
        self.xl_lines_header = text.strip()

    def edit_filename_header_text_changed(self, text):
        self.xl_filename_header = text.strip()

    def edit_lang_header_text_changed(self, text):
        self.xl_lang_header = text.strip()

    def load_xl(self):
        wb = load_workbook(self.xl_path, data_only=True)
        ws = wb.active

        data = []
        text_index = None
        lang_index = None
        filename_index = None
        is_header = True

        for i in ws.values:
            if is_header:
                text_index = i.index('台词')
                filename_index = i.index('文件名')
                lang_index = i.index('语言')
                is_header = False
                continue

            text = i[text_index]
            if text is None:
                continue
            else:
                text = str(text).strip()
                if not text: continue

            filename = i[filename_index]
            if filename is None:
                continue
            else:
                filename = str(filename).strip()
                if not filename: continue

            lang = i[lang_index]
            if lang is None:
                lang = ''
            else:
                lang = str(lang).strip()
                if lang not in self.lang_list: continue

            data.append([text, filename, lang])

        return data

    def btn_xl_save_clicked(self):
        if not Path(self.xl_path).is_file():
            QMessageBox.warning(self, '警告', f'文件不存在！\n{self.xl_path}')
            return
        try:
            data = self.load_xl()
        except Exception as e:
            QMessageBox.warning(self, '警告', f'表格解析失败\n{e}')
            return
        save_path = self.edit_xl_save_path.text().strip()
        text_list = []
        if save_path:
            if not Path(save_path).exists():
                Path(save_path).mkdir(parents=True)
            for text, filename, lang in data:
                if not lang: lang = self.lang
                text_list.append([text, str(Path(save_path) / filename), lang])
        else:
            text_list = data

        self.tts_from_list(data)
        QMessageBox.information(self, '信息', '成功生成语音！')

    def comb_lang_text_activated(self, text):
        self.lang = text


app = QApplication()
window = Window()
window.show()
app.exec()

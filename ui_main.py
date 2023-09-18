# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDoubleSpinBox, QFormLayout,
    QGroupBox, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QSpacerItem, QStatusBar,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(601, 515)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox_4 = QGroupBox(self.centralwidget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(300, 0, 281, 231))
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.edit_text_input = QTextEdit(self.groupBox_4)
        self.edit_text_input.setObjectName(u"edit_text_input")

        self.verticalLayout_3.addWidget(self.edit_text_input)

        self.edit_save_path = QLineEdit(self.groupBox_4)
        self.edit_save_path.setObjectName(u"edit_save_path")

        self.verticalLayout_3.addWidget(self.edit_save_path)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_6 = QLabel(self.groupBox_4)
        self.label_6.setObjectName(u"label_6")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label_6)

        self.comb_lang = QComboBox(self.groupBox_4)
        self.comb_lang.setObjectName(u"comb_lang")

        self.horizontalLayout_2.addWidget(self.comb_lang)

        self.btn_save = QPushButton(self.groupBox_4)
        self.btn_save.setObjectName(u"btn_save")

        self.horizontalLayout_2.addWidget(self.btn_save)

        self.btn_play = QPushButton(self.groupBox_4)
        self.btn_play.setObjectName(u"btn_play")

        self.horizontalLayout_2.addWidget(self.btn_play)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.groupBox_5 = QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(300, 230, 281, 241))
        self.verticalLayout_4 = QVBoxLayout(self.groupBox_5)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.formLayout_3 = QFormLayout()
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.label_4 = QLabel(self.groupBox_5)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_3.setWidget(1, QFormLayout.LabelRole, self.label_4)

        self.edit_lines_header = QLineEdit(self.groupBox_5)
        self.edit_lines_header.setObjectName(u"edit_lines_header")

        self.formLayout_3.setWidget(1, QFormLayout.FieldRole, self.edit_lines_header)

        self.label_5 = QLabel(self.groupBox_5)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_3.setWidget(2, QFormLayout.LabelRole, self.label_5)

        self.edit_filename_header = QLineEdit(self.groupBox_5)
        self.edit_filename_header.setObjectName(u"edit_filename_header")

        self.formLayout_3.setWidget(2, QFormLayout.FieldRole, self.edit_filename_header)

        self.btn_load_xl = QPushButton(self.groupBox_5)
        self.btn_load_xl.setObjectName(u"btn_load_xl")

        self.formLayout_3.setWidget(0, QFormLayout.LabelRole, self.btn_load_xl)

        self.edit_xl = QLineEdit(self.groupBox_5)
        self.edit_xl.setObjectName(u"edit_xl")

        self.formLayout_3.setWidget(0, QFormLayout.FieldRole, self.edit_xl)

        self.label_7 = QLabel(self.groupBox_5)
        self.label_7.setObjectName(u"label_7")
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)

        self.formLayout_3.setWidget(3, QFormLayout.LabelRole, self.label_7)

        self.edit_lang_header = QLineEdit(self.groupBox_5)
        self.edit_lang_header.setObjectName(u"edit_lang_header")

        self.formLayout_3.setWidget(3, QFormLayout.FieldRole, self.edit_lang_header)


        self.verticalLayout_4.addLayout(self.formLayout_3)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.edit_xl_save_path = QLineEdit(self.groupBox_5)
        self.edit_xl_save_path.setObjectName(u"edit_xl_save_path")

        self.verticalLayout_4.addWidget(self.edit_xl_save_path)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.btn_xl_save = QPushButton(self.groupBox_5)
        self.btn_xl_save.setObjectName(u"btn_xl_save")

        self.horizontalLayout_3.addWidget(self.btn_xl_save)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 0, 278, 469))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.groupBox = QGroupBox(self.layoutWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.btn_load_model = QPushButton(self.groupBox)
        self.btn_load_model.setObjectName(u"btn_load_model")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.btn_load_model)

        self.edit_model = QLineEdit(self.groupBox)
        self.edit_model.setObjectName(u"edit_model")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.edit_model)

        self.btn_load_config = QPushButton(self.groupBox)
        self.btn_load_config.setObjectName(u"btn_load_config")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.btn_load_config)

        self.edit_config = QLineEdit(self.groupBox)
        self.edit_config.setObjectName(u"edit_config")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.edit_config)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(self.layoutWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.formLayout_2 = QFormLayout(self.groupBox_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label = QLabel(self.groupBox_2)
        self.label.setObjectName(u"label")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label)

        self.spin_length = QDoubleSpinBox(self.groupBox_2)
        self.spin_length.setObjectName(u"spin_length")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.spin_length)

        self.label_2 = QLabel(self.groupBox_2)
        self.label_2.setObjectName(u"label_2")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.spin_noise = QDoubleSpinBox(self.groupBox_2)
        self.spin_noise.setObjectName(u"spin_noise")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.spin_noise)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.spin_noise_w = QDoubleSpinBox(self.groupBox_2)
        self.spin_noise_w.setObjectName(u"spin_noise_w")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.spin_noise_w)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.groupBox_3 = QGroupBox(self.layoutWidget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.verticalLayout = QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_search_pre = QPushButton(self.groupBox_3)
        self.btn_search_pre.setObjectName(u"btn_search_pre")

        self.horizontalLayout.addWidget(self.btn_search_pre)

        self.btn_search_next = QPushButton(self.groupBox_3)
        self.btn_search_next.setObjectName(u"btn_search_next")

        self.horizontalLayout.addWidget(self.btn_search_next)

        self.edit_speaker = QLineEdit(self.groupBox_3)
        self.edit_speaker.setObjectName(u"edit_speaker")

        self.horizontalLayout.addWidget(self.edit_speaker)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.list_widget_speaker = QListWidget(self.groupBox_3)
        self.list_widget_speaker.setObjectName(u"list_widget_speaker")

        self.verticalLayout.addWidget(self.list_widget_speaker)


        self.verticalLayout_2.addWidget(self.groupBox_3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 601, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.groupBox_4.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u672c\u8f93\u5165", None))
        self.edit_save_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u6587\u4ef6", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u8bed\u8a00", None))
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"\u5408\u6210", None))
        self.btn_play.setText(QCoreApplication.translate("MainWindow", u"\u64ad\u653e", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("MainWindow", u"\u8bfb\u8868\u751f\u6210", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u8868\u5934-\u53f0\u8bcd", None))
        self.edit_lines_header.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u53f0\u8bcd", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u8868\u5934-\u6587\u4ef6\u540d", None))
        self.edit_filename_header.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6\u540d", None))
        self.btn_load_xl.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6587\u4ef6", None))
        self.edit_xl.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Excel \u6587\u4ef6(*.xlsx)", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u8868\u5934-\u8bed\u8a00", None))
        self.edit_lang_header.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bed\u8a00", None))
        self.edit_xl_save_path.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u8def\u5f84", None))
        self.btn_xl_save.setText(QCoreApplication.translate("MainWindow", u"\u8bfb\u8868\u751f\u6210", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u6a21\u578b", None))
        self.btn_load_model.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6a21\u578b", None))
        self.edit_model.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u6587\u4ef6", None))
        self.btn_load_config.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u914d\u7f6e", None))
        self.edit_config.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u914d\u7f6e\u6587\u4ef6", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MainWindow", u"\u53c2\u6570", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u65f6\u957f\u6bd4\u4f8b", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u566a\u58f0\u6bd4\u4f8b", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u566a\u58f0\u504f\u5dee", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("MainWindow", u"\u8bf4\u8bdd\u4eba", None))
        self.btn_search_pre.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22<", None))
        self.btn_search_next.setText(QCoreApplication.translate("MainWindow", u"\u641c\u7d22>", None))
        self.edit_speaker.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u89d2\u8272\u540d\u79f0", None))
    # retranslateUi


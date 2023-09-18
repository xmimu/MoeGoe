from scipy.io.wavfile import write
from mel_processing import spectrogram_torch
from text import text_to_sequence, _clean_text
from models import SynthesizerTrn
import utils
import commons
import sys
import re
from torch import no_grad, LongTensor
import logging

logging.getLogger('numba').setLevel(logging.WARNING)


def get_text(text, hps, cleaned=False):
    if cleaned:
        text_norm = text_to_sequence(text, hps.symbols, [])
    else:
        text_norm = text_to_sequence(text, hps.symbols, hps.data.text_cleaners)
    if hps.data.add_blank:
        text_norm = commons.intersperse(text_norm, 0)
    text_norm = LongTensor(text_norm)
    return text_norm


def ask_if_continue():
    while True:
        answer = input('Continue? (y/n): ')
        if answer == 'y':
            break
        elif answer == 'n':
            sys.exit(0)


def get_speaker_id(message):
    speaker_id = input(message)
    try:
        speaker_id = int(speaker_id)
    except:
        print(str(speaker_id) + ' is not a valid ID!')
        sys.exit(1)
    return speaker_id


def get_label_value(text, label, default, warning_name='value'):
    value = re.search(rf'\[{label}=(.+?)\]', text)
    if value:
        try:
            text = re.sub(rf'\[{label}=(.+?)\]', '', text, 1)
            value = float(value.group(1))
        except:
            print(f'Invalid {warning_name}!')
            sys.exit(1)
    else:
        value = default
    return value, text


def get_label(text, label):
    if f'[{label}]' in text:
        return True, text.replace(f'[{label}]', '')
    else:
        return False, text


def load_model(model, config):
    hps_ms = utils.get_hparams_from_file(config)
    n_speakers = hps_ms.data.n_speakers if 'n_speakers' in hps_ms.data.keys() else 0
    n_symbols = len(hps_ms.symbols) if 'symbols' in hps_ms.keys() else 0
    speakers = hps_ms.speakers if 'speakers' in hps_ms.keys() else ['0']
    use_f0 = hps_ms.data.use_f0 if 'use_f0' in hps_ms.data.keys() else False
    emotion_embedding = hps_ms.data.emotion_embedding if 'emotion_embedding' in hps_ms.data.keys() else False

    net_g_ms = SynthesizerTrn(
        n_symbols,
        hps_ms.data.filter_length // 2 + 1,
        hps_ms.train.segment_size // hps_ms.data.hop_length,
        n_speakers=n_speakers,
        emotion_embedding=emotion_embedding,
        **hps_ms.model)
    _ = net_g_ms.eval()
    utils.load_checkpoint(model, net_g_ms)
    print(f'Loaded model: {model}')
    return speakers, n_symbols, emotion_embedding, hps_ms, net_g_ms


def model_tts(speaker_id, text, out_path, hps_ms, net_g_ms,
              length_scale=1, noise_scale=0.667, noise_scale_w=0.8
              ):
    cleaned, text = get_label(text, 'CLEANED')
    stn_tst = get_text(text, hps_ms, cleaned=cleaned)

    with no_grad():
        x_tst = stn_tst.unsqueeze(0)
        x_tst_lengths = LongTensor([stn_tst.size(0)])
        sid = LongTensor([speaker_id])
        audio = net_g_ms.infer(
            x_tst, x_tst_lengths, sid=sid, noise_scale=noise_scale,
            noise_scale_w=noise_scale_w, length_scale=length_scale
        )[0][0, 0].data.cpu().float().numpy()

    write(out_path, hps_ms.data.sampling_rate, audio)
    print(f'Successfully saved! - {out_path}')


if __name__ == '__main__':
    model = r'C:\Users\Administrator\Downloads\hotta_ganzhe(2000epoch)\G_399000.pth'
    config = r'C:\Users\Administrator\Downloads\hotta_ganzhe(2000epoch)\config.json'
    n_symbols, emotion_embedding, hps_ms, net_g_ms = load_model(model, config)
    if n_symbols != 0:
        if not emotion_embedding:
            text_list = ['你好', '今天好吗', '明天去吃饭吗']
            for idx, i in enumerate(text_list):
                model_tts(0, i, f'{idx}.wav', hps_ms, net_g_ms)

        else:
            print('emotion_embedding...')
    else:
        print('n_symbols == 0')

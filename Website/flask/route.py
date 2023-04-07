from flask import Flask
from flask import redirect, render_template, request, flash
import os
import nemo.collections.asr as nemo_asr
import nemo.collections.nlp as nemo_nlp
import nemo.collections.tts as nemo_tts
from transformers import pipeline
import re
import soundfile as sf

from application import app

app.config["AUDIO_UPLOADS"] = "audio"
app.config["MODEL_FILES"] = "models"

class all_models():
    def __init__(self):
        self.puncbert = nemo_nlp.models.PunctuationCapitalizationModel.restore_from(restore_path=os.path.join(app.config["MODEL_FILES"], "punc_bert.nemo"))
        self.conformer = nemo_asr.models.EncDecCTCModel.restore_from(restore_path=os.path.join(app.config["MODEL_FILES"], "conformer_transducer.nemo"))
        self.spec_generator = nemo_tts.models.FastPitchModel.restore_from(restore_path=os.path.join(app.config["MODEL_FILES"], "fastpitch.nemo"))
        self.hifigan = nemo_tts.models.HifiGanModel.restore_from(restore_path=os.path.join('Website/models', "hifigan.nemo"))
        self.text_classifier = classifier = pipeline("text-classification", model="bhadresh-savani/bert-base-go-emotion")

models = all_models()

@app.route("/transcribe", methods=['GET', 'POST'])
def asr():
    if request.method == "POST":
        if request.files:
            audio_file = request.files["audiofile"]
            audio_file.save(os.path.join(app.config["AUDIO_UPLOADS"], audio_file.filename))
            transcribed_text = models.conformer(audio_file.filename)
            punc_text = models.puncbert(transcribed_text[0])
            remove_last_index = False
            if (punc_text[0][-1] == '.') | (punc_text[0][-1] == '!') | (punc_text[0][-1] == '?'):
                remove_last_index = True

            annotated_text = label_sentences(punc_text, remove_last_index)

            
def label_sentences(sentences, remove_last_index):
    sentence_dict = {}
    sentence_split = re.split(['.?!'], sentences)
    if remove_last_index:
        for index, sentence in enumerate(sentence_split):
            if index < len(sentence_split)-1:
                sentence_dict[sentence] = models.text_classifier(sentence)[0]['label']
    else:
        for index, sentence in enumerate(sentence_split):
            if index < len(sentence_split):
                sentence_dict[sentence] = models.text_classifier(sentence)[0]['label']

    ann_text =f''
    for sentence in sentence_dict:
        ann_text+=(f'{sentence}[{sentence_dict[sentence]}]')
    print(ann_text)
    return ann_text

def use_tts(text):
    parsed_text = models.spec_generator.parse(text)
    spectrogram = models.spec_generator.generate_spectrogram(tokens=parsed_text)
    prompt_audio = models.hifigan.convert_spectrogram_to_audio(spec=spectrogram)
    sf.write(os.path.join(app.config["AUDIO_UPLOADS"], "currentaudio"), prompt_audio.to('cpu').detach().numpy()[0], 22050)

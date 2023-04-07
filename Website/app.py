
from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import tensorflow as tf
import librosa
import numpy as np
import re
from sqlalchemy import create_engine
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)

CORS(app, origins=['http://localhost:3000'])

#Load Models
db_username = "root"
db_password = "brod"
db_host = "localhost"
db_name = "speechedtech"
db_uri = f"mysql://{db_username}:{db_password}@{db_host}/{db_name}"


app.config["SQLALCHEMY_DATABASE_URI"]=db_uri
app.config["AUDIO_UPLOADS"] = "audio"
app.config["MODEL_FILES"] = "models"
db=SQLAlchemy(app)
# class all_models():
#     def __init__(self):
#         self.puncbert = nemo_nlp.models.PunctuationCapitalizationModel.restore_from(restore_path=os.path.join(app.config["MODEL_FILES"], "punc_bert.nemo"))
#         self.conformer = nemo_asr.models.EncDecCTCModel.restore_from(restore_path=os.path.join(app.config["MODEL_FILES"], "conformer_transducer.nemo"))
#         self.spec_generator = nemo_tts.models.FastPitchModel.restore_from(restore_path=os.path.join(app.config["MODEL_FILES"], "fastpitch.nemo"))
#         self.hifigan = nemo_tts.models.HifiGanModel.restore_from(restore_path=os.path.join('Website/models', "hifigan.nemo"))
#         self.text_classifier = classifier = pipeline("text-classification", model="bhadresh-savani/bert-base-go-emotion")
#         self.SEC_model = tf.keras.models.load_model('./Models/SEC_model.h5')

# models = all_models()

# @app.route("/transcribe", methods=['GET', 'POST'])
# def asr():
#     if request.method == "POST":
#         if request.files:
#             audio_file = request.files["audiofile"]
#             audio_file.save(os.path.join(app.config["AUDIO_UPLOADS"], audio_file.filename))
#             transcribed_text = models.conformer(audio_file.filename)
#             punc_text = models.puncbert(transcribed_text[0])
#             remove_last_index = False
#             if (punc_text[0][-1] == '.') | (punc_text[0][-1] == '!') | (punc_text[0][-1] == '?'):
#                 remove_last_index = True

#             annotated_text = label_sentences(punc_text, remove_last_index)




class Questions(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Passage = db.Column(db.Text, nullable=False)
    Level = db.Column(db.String(255), nullable=False)
    Difficulty = db.Column(db.String(45), nullable=False)


#SEC preprocessing
def noise(data):
    noise_amp = 0.04*np.random.uniform()*np.amax(data)
    data = data + noise_amp*np.random.normal(size=data.shape[0])
    return data

def stretch(data, rate=0.70):
    return librosa.effects.time_stretch(data,rate=rate)

def shift(data):
    shift_range = int(np.random.uniform(low=-5, high = 5)*1000)
    return np.roll(data, shift_range)

def pitch(data, sampling_rate, pitch_factor=0.7):
    return librosa.effects.pitch_shift(data, sr=sampling_rate, n_steps=pitch_factor)

def higher_speed(data, speed_factor = 1.25):
    return librosa.effects.time_stretch(data,rate=speed_factor)

def lower_speed(data, speed_factor = 0.75):
    return librosa.effects.time_stretch(data,rate=speed_factor)

def extract_features(data):
    
    result = np.array([])
    
    mfccs = librosa.feature.mfcc(y=data, sr=22050, n_mfcc=58)
    mfccs_processed = np.mean(mfccs.T,axis=0)
    result = np.array(mfccs_processed)
     
    return result

def get_features(path):
    # duration and offset are used to take care of the no audio in start and the ending of each audio files as seen above.
    data, sample_rate = librosa.load(path, duration=3, offset=0.5) 
    
    #without augmentation
    res1 = extract_features(data)
    result = np.array(res1)
    
    #noised
    noise_data = noise(data)
    res2 = extract_features(noise_data)
    result = np.vstack((result, res2)) # stacking vertically
    
    #stretched
    stretch_data = stretch(data)
    res3 = extract_features(stretch_data)
    result = np.vstack((result, res3))
    
    #shifted
    shift_data = shift(data)
    res4 = extract_features(shift_data)
    result = np.vstack((result, res4))
    
    #pitched
    pitch_data = pitch(data, sample_rate)
    res5 = extract_features(pitch_data)
    result = np.vstack((result, res5)) 
    
    #speed up
    higher_speed_data = higher_speed(data)
    res6 = extract_features(higher_speed_data)
    result = np.vstack((result, res6))
    
    #speed down
    lower_speed_data = higher_speed(data)
    res7 = extract_features(lower_speed_data)
    result = np.vstack((result, res7))
    
    return result
#----------------------------------------------------------------------------------
# Load the model from the .h5 file
SEC_model = tf.keras.models.load_model('./Models/SEC_model.h5')

sec_labels=['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']

@app.route('/predict', methods=['POST'])
def predict():
  # Get the uploaded file
  # Get the uploaded file
  audio_file = request.files['audio']
  questions = Questions.query.all()
  with open('questions.txt', 'w') as f:
    # loop through the results and write each row to the file
    for row in questions:
        f.write(f"Passage: {row.Passage}\nLevel: {row.Level}\nDifficulty: {row.Difficulty}\n\n")
  # Define the file path where the audio file will be saved
  audio_file.save('recording.wav')
  print(os.getcwd())
  x=get_features("recording.wav")

  x=np.expand_dims(x, axis=2)
  os.remove('recording.wav')
  prediction=SEC_model.predict(x)
  prediction=np.argmax(prediction[0])

  # Save the file to disk
#   audio_file.save('recording.wav')
    
  # Process audio data here

  result = {'emotion': sec_labels[prediction]}
  print(result)
  return jsonify(result)

@app.route('/questions/<level>', methods=['GET'])
def get_questions_by_level(level):
    questions = Questions.query.all()
    results = [
        {
            "id": question.id,
            "Passage": question.Passage,

        }
        for question in questions if question.Level == level
    ]
    
    return jsonify(results)

if __name__ == '__main__':
    app.run(host='localhost', port=3001)



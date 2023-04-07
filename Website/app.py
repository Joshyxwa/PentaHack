from flask import Flask, request, jsonify
from flask_cors import CORS
import os
import tensorflow as tf
import librosa
import numpy as np
from pydub import AudioSegment


app = Flask(__name__)

CORS(app, origins=['http://localhost:3000'])

#Load Models


# Load the model from the .h5 file
SEC_model = tf.keras.models.load_model('./Models/SEC_model.h5')

sec_labels=['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']

@app.route('/predict', methods=['POST'])
def predict():
  # Get the uploaded file
  # Get the uploaded file
  audio_file = request.files['audio']

  # Define the file path where the audio file will be saved
  audio_file.save('recording.mp3')
  print(os.getcwd())
  audio_data, sample_rate = librosa.load('recording.mp3')   
  mfccs = librosa.feature.mfcc(y=audio_data, sr=22050, n_mfcc=58)
  print("james")
  mfccs_processed = np.mean(mfccs.T,axis=0)
  print("james")
  x = np.array(mfccs_processed)
  os.remove('recording.mp3')
  prediction=SEC_model.predict(x)
  # Save the file to disk
#   audio_file.save('recording.wav')
    
  # Process audio data here
  predicted_emotion = 'happy'
  result = {'emotion': sec_labels[prediction]}
  print(result)
  return jsonify(result)


if __name__ == '__main__':
    app.run(host='localhost', port=3001)

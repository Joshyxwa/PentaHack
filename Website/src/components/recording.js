import React, { useState, useEffect } from 'react';
import './recording.css';
//['angry', 'disgust', 'fear', 'happy', 'neutral', 'sad', 'surprise']
function Recorder() {
  const [recording, setRecording] = useState(false);
  const [audioURL, setAudioURL] = useState('');
  const [error, setError] = useState(null);
  const [timer, setTimer] = useState(0);
  const [mediaRecorder, setMediaRecorder] = useState(null);
  const [intervalID, setIntervalID] = useState(null);
  

  useEffect(() => {
    if (mediaRecorder) {
      mediaRecorder.ondataavailable = handleDataAvailable;
      mediaRecorder.onstop = handleStop;
    }
  }, [mediaRecorder]);

  function handleDataAvailable(e) {
    const audioBlob = new Blob([e.data], { type: 'audio/wav' });
    const url = URL.createObjectURL(audioBlob);
    setAudioURL(url);
  }

  function handleStop() {
    setRecording(false);
    clearInterval(intervalID);
  }

  function startRecording() {
    navigator.mediaDevices.getUserMedia({ audio: true })
      .then(stream => {
        const mediaRecorder = new MediaRecorder(stream);
        setMediaRecorder(mediaRecorder);
        mediaRecorder.start();
        setRecording(true);
        setTimer(0);
        const interval = setInterval(() => setTimer(prev => prev + 1), 1000);
        setIntervalID(interval);
      })
      .catch(err => setError(err.message));
  }

  function stopRecording() {
    mediaRecorder.stop();
  }

  function retryRecording() {
    setAudioURL('');
    setTimer(0);
    setRecording(false);
    clearInterval(intervalID);
  }
  function submitRecording() {
    // If there is no audio to submit, return
    if (!audioURL) return;

    // Convert the recorded audio blob to a File object
    fetch(audioURL)
      .then(response => response.blob())
      .then(audioBlob => {
        // Create a new File object from the audio blob
        const file = new File([audioBlob], 'recording.wav', {
          type: 'audio/wav',
          lastModified: Date.now()
        });

        // Create a FormData object and append the file to it
        const formData = new FormData();
        formData.append('audio', file);

        // Send the FormData object to the server using the fetch() function
        fetch('http://localhost:3001/predict', {
          method: 'POST',
          body: formData
        })
          .then(response => response.json())
          .then(data => {
            console.log('Server response:', data);
            const predictedEmotion = data.emotion;
            console.log(predictedEmotion)
            // Do something with the predicted emotion value
          })
          .catch(error => {
            console.error('Error submitting audio recording:', error);
            // handle error as needed
          });
      })
      .catch(error => {
        console.error('Error extracting audio data:', error);
        // handle error as needed
      });
  }

  

  return (
    <div className="recorder-container">
      {recording ? (
        <>
          <button onClick={stopRecording}>Stop Recording</button>
          <p>Recording duration: {timer} seconds</p>
        </>
      ) : (
        <>
          {audioURL ? (
            <>
              <audio src={audioURL} controls />
              <div className="button-container">
                <button onClick={retryRecording} style={{ marginRight: '10px' }}>Retry Recording</button>
                <button onClick={submitRecording}>Submit Recording</button>
              </div>
            </>
          ) : (
            <>
              <button onClick={startRecording}>Start Recording</button>
              <p>{error}</p>
            </>
          )}
        </>
      )}
    </div>
  );

}

export default Recorder;

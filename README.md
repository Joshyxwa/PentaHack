# PentaHack

## Introduction
This repository is our group's work on the PentaHack Hackathon 2023 on the topic of "AI in Education". Our solution consists of multiple AI technology ranging from Automatic Speech Recognition (ASR), Natural Language Processing (NLP), and Text to Speech (TTS).

## How to setup

1) Run the docker command. This is important as linux environment is a requirement to host NeMo models.
```
docker run -tid -v /var/run/docker.sock:/var/run/docker.sock  --name penta_con nvcr.io/nvidia/nemo:23.01
```
2) Open the docker container in an IDE.

3) git clone this repository
```
git clone https://github.com/Joshyxwa/PentaHack.git
```

4) Download the package requirements, nodejs and npm for React
```
pip install -r requirements.txt
sudo apt update
sudo apt install nodejs
sudo apt install npm
```

5) Download all the NeMo models from the download_model.py
```
python download_nemo_models.py
```

6) To install react, run
```
npm install
```

7) To run the application, run
```
npm run start
```

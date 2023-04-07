from nvcr.io/nvidia/nemo:23.01
RUN apt-get update && apt-get upgrade -y
ENV DEBIAN_FRONTEND=noninteractive
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apt-get update
RUN \
  apt-get update && \
  apt-get install -y sudo curl git libsndfile1 && \
  curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash && \
  sudo apt-get install git-lfs && \
  mkdir -p /src 
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY . /code
CMD ["flask", "run"]
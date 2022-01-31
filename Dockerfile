FROM python:latest
WORKDIR .
RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip ffmpeg -y
RUN pip3 install -U pip
RUN pip3 install -U -r requirements.txt
COPY music.py .
COPY . .
CMD ["bash", "ultron.sh"]

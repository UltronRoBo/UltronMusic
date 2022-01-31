FROM python:3.9
WORKDIR .
RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip ffmpeg -y
COPY music.py .
COPY requirements.txt .
RUN pip3 install -U pip
RUN pip3 install -U -r requirements.txt
COPY . .
CMD ["bash", "ultron.sh"]

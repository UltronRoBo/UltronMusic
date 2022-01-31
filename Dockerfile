FROM python:latest
WORKDIR .
RUN apt update && apt upgrade -y
RUN apt install git curl python3-pip ffmpeg -y
COPY . .
RUN pip3 install -U pip
RUN pip3 install -U -r requirements.txt
CMD ["bash", "ultron.sh"]

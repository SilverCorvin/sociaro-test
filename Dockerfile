FROM python:3.5

MAINTAINER Ivan.Povalyaev@gmail.com

ADD requirements.txt /app/requirements.txt
WORKDIR /app/
RUN echo "deb http://www.deb-multimedia.org jessie main non-free" >> /etc/apt/sources.list
RUN echo "deb-src http://www.deb-multimedia.org jessie main non-free" >> /etc/apt/sources.list
RUN apt-get update -y
RUN apt-get install -y --force-yes ffmpeg
RUN pip install -r requirements.txt
RUN adduser --disabled-password --gecos '' test

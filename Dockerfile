# syntax=docker/dockerfile:1

FROM python:3
EXPOSE 8000
ENV PYTHONBUFFERED=1 PYTHONDONTWRITEBYTECODE=1

#RUN apt-get -y update
#RUN apt-get install -y cron && touch /var/log/cron.log

COPY . /opt/coinmena
WORKDIR /opt/coinmena

#COPY requirements.txt /opt/coinmena
RUN pip install -r requirements.txt


RUN useradd appuser && chown -R appuser /opt/coinmena
USER appuser

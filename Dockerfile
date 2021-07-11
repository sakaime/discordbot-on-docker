FROM python:3.9.4-buster

RUN mkdir /app
WORKDIR /app

COPY requirements.txt /app

ENV PYTHONUNBUFFERED 1
ENV PYTHONUSERBASE /app/vendor
ENV PATH $PATH:$PYTHONUSERBASE/bin

RUN apt-get update && \
  pip install --upgrade pip && \
  pip install --upgrade setuptools && \
  pip install -r requirements.txt --user

COPY . /app
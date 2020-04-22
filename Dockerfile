FROM python:3.7-buster

RUN mkdir /code/
WORKDIR /code/
COPY . /code/

RUN pip3 install -r requirements.txt
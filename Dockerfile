FROM python:3.9

ENV PYTHONUNBUFFERED 1

WORKDIR /lunch_decision

COPY requirements.txt /lunch_decision/

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /lunch_decision/

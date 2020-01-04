FROM python:3.8-alpine3.10
ENV PYTHONUNBUFFERED 1
WORKDIR /usr/src
COPY requirements.txt /usr/src/
RUN pip install -r requirements.txt
COPY . /usr/src/
WORKDIR /usr/src/backend
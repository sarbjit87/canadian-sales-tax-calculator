FROM python:3.8.1-alpine

RUN mkdir /src
WORKDIR /src

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt

RUN set -eux \
    && apk add --no-cache --virtual .build-deps build-base \
       libressl-dev libffi-dev gcc musl-dev python3-dev \
    && pip install --upgrade pip setuptools wheel \
    && pip install -r /requirements.txt \
    && rm -rf /root/.cache/pip

COPY ./src /src

RUN adduser -D user
USER user

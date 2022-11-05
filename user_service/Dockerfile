FROM python:3.10-alpine3.16
LABEL maintainer = "user"

ENV PYTHONUNBUFFERED 1

ARG DEV=false
EXPOSE 8000


RUN apk add --update --no-cache postgresql-client jpeg-dev && \
    apk add --update --no-cache --virtual .tmp-build-deps \
        build-base postgresql-dev musl-dev zlib zlib-dev linux-headers


COPY . /usr/src/app
WORKDIR /usr/src/app/user_service

RUN pip install --upgrade pip &&\
	pip install pipenv

RUN pipenv install --system




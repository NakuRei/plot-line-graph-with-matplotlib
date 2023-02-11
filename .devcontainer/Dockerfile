FROM python:3-slim-bullseye

USER root

RUN apt update -y \
    && apt upgrade -qqy

RUN apt install -y locales && \
    localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm

RUN apt update -y \
    && apt install -y \
    git \
    fonts-ricty-diminished

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

ENTRYPOINT [ "/bin/bash" ]

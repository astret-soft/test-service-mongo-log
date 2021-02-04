FROM python:3.8-slim-buster

MAINTAINER "Astretsov Artem"
LABEL project="service_mongo_log"
LABEL version = "0.1"
LABEL author="Astretsov Artem"

ADD mongo_log/requirements.txt /requirements.txt

RUN pip install --no-cache-dir --upgrade && \
    sed -i '/# TEST/q' requirements.txt && \
    pip install --no-cache-dir -r requirements.txt && \
    find /usr/local \
        -o \( -type f -a -name '*.pyc' -o -name '*.pyo' \) \
        -exec rm -rf '{}' + && \
    apk del build-base linux-headers && \
    rm /requirements.txt && \
    rm /.pylintrc

WORKDIR /app

COPY ./app /app

EXPOSE 65333
ENTRYPOINT python /app/main.py

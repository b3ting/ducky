# syntax=docker/dockerfile:1.4

FROM --platform=$BUILDPLATFORM python:3.7-alpine AS builder
EXPOSE 8000
WORKDIR /app 

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add --no-cache mariadb-dev

COPY requirements.txt /app
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /app 
# CMD ["python3", "main.py"]
CMD ["gunicorn", "-b", "0.0.0.0:8000", "main:app"]

#ENTRYPOINT ["gunicorn --worker-class eventlet -w 1 wsgi:app"]
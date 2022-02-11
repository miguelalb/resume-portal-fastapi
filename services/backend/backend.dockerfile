FROM python:3.9-buster

RUN mkdir app
WORKDIR /app

ENV PATH="${PATH}:/root/.local/bin"

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
    && apt-get -y install netcat gcc postgresql \
    && apt-get clean

COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./app /app
ENV PYTHONPATH=/app

COPY ./entrypoint.sh .
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT [ "/app/entrypoint.sh" ]
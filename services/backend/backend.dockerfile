FROM tiangolo/uvicorn-gunicorn-fastapi:python3.7

RUN mkdir app
WORKDIR /app

COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY ./app /app
ENV PYTHONPATH=/app

FROM python:3.6
WORKDIR /app
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY . .
ENTRYPOINT celery -A worker worker --autoscale 10 --loglevel=info
FROM python:3.9.0

ENV PYTHONUNBUFFERED 1

WORKDIR /drf
COPY . .

RUN apt-get update
RUN apt-get install -y  cron
RUN pip install --no-cache-dir -r requirements.txt
RUN mkdir /tmp/log
RUN ln -snf /usr/share/zoneinfo/Asia/Seoul /etc/localtime
RUN python manage.py crontab add

CMD cron && gunicorn config.wsgi:application --bind 0.0.0.0:8000

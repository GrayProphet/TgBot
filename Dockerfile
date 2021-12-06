FROM python:3

WORKDIR /usr/src/app

RUN pip install aiogram

COPY config.py .
COPY main.py .

CMD [ "python3", "./main.py"]
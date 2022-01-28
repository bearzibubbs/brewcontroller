FROM docker.io/arm32v7/python:3.10.1-bullseye

WORKDIR /opt/brewcontroller/

ENV CFLAGS=-fcommon

#RUN ["apt", "install", "python3-setuptools"]

RUN ["python", "-m", "pip", "install", "--no-cache-dir", "-r", "requirements.txt"]


ENV FLASK_APP=pid_api
ENV FLASK_ENV=development

COPY . .

CMD ["flask", "run", "--host=0.0.0.0"]
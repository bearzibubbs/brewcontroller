FROM docker.io/arm32v7/python:3.10.1-bullseye

WORKDIR /opt/brewcontroller/

COPY . .

RUN ["apt", "install", "setuptools"]

RUN ["python", "-m", "pip", "install", "-r", "requirements.txt"]


ENV FLASK_APP=pid_api
ENV FLASK_ENV=development

CMD ["flask", "run"]
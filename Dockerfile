FROM arm32v7/python:3.10.1

WORKDIR /opt/brewcontroller/

COPY . .

RUN ["python", "-m", "pip", "install", "-r", "requirements.txt"]

ENV FLASK_APP=pid_api
ENV FLASK_ENV=development

CMD ["flask", "run"]
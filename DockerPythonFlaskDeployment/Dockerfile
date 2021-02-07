FROM python:3.6.1-alpine

WORKDIR /DockerPythonFlaskDeployment

ADD . /DockerPythonFlaskDeployment

RUN pip install -r requirements.txt

CMD ["python", "test.py"]


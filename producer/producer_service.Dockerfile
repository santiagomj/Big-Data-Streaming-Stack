FROM python:3.9.10

WORKDIR /usr/app/src
COPY . ./

ARG DEBIAN_FRONTEND=noninteractive

RUN cat /etc/os-release

RUN apt-get update && apt-get install software-properties-common -y

RUN wget -qO - http://packages.confluent.io/deb/3.2/archive.key | apt-key add -

RUN add-apt-repository "deb [arch=amd64] http://packages.confluent.io/deb/3.2 stable main"
RUN apt-get update && apt-get install confluent-platform-oss-2.11 -y

RUN apt-get update && apt install librdkafka-dev -y

RUN apt-get update && pip install -r producer_service_requirements.txt

CMD [ "python", "-u", "./crypto_producer.py"]
FROM jupyter/pyspark-notebook:8ea7abc5b7bc
USER root
ENV PYSPARK_SUBMIT_ARGS '--packages org.apache.spark:spark-avro_2.12:3.0.1,org.apache.spark:spark-sql-kafka-0-10_2.12:3.0.1,org.apache.spark:spark-streaming-kafka-0-10_2.12:3.0.1,io.delta:delta-core_2.12:1.1.0,com.amazonaws:aws-java-sdk:1.11.950,org.apache.hadoop:hadoop-aws:3.2.0,net.java.dev.jets3t:jets3t:0.9.4 pyspark-shell'

COPY ./delta_spark_jupyter /src
WORKDIR /src
#spark
ARG DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install build-essential -y
RUN apt-get update && apt-get install -y python3-pip python3-dev
RUN apt-get install -y curl
RUN curl -O https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/1.11.950/aws-java-sdk-bundle-1.11.950.jar
RUN curl -O https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/3.2.0/hadoop-aws-3.2.0.jar
RUN curl -O https://repo1.maven.org/maven2/net/java/dev/jets3t/jets3t/0.9.4/jets3t-0.9.4.jar

RUN \
  apt-get update && \
  apt-get install -y openjdk-8-jdk && \
  rm -rf /var/lib/apt/lists/*

RUN apt-get update && apt-get install software-properties-common -y

RUN wget -qO - http://packages.confluent.io/deb/3.2/archive.key | apt-key add -

RUN add-apt-repository "deb [arch=amd64] http://packages.confluent.io/deb/3.2 stable main"
RUN apt-get update && apt-get install confluent-platform-oss-2.11 -y

RUN apt-get update && apt install librdkafka-dev -y

RUN pip install -r requirements.txt

CMD ["bash"]
import requests
import json
import uuid
import os
from time import sleep

from confluent_kafka.avro import AvroProducer
from confluent_kafka import avro

from map_avro_types import avro_value_schema_to_python_types

TOPIC = os.getenv("TOPIC")
BOOTSTRAP_SERVERS = os.getenv("BOOTSTRAP_SERVERS")
SCHEMA_REGISTRY = os.getenv("SCHEMA_REGISTRY")
SCHEMA_FILE = os.getenv("SCHEMA_FILE")
KEY_SCHEMA_STRING = os.getenv("KEY_SCHEMA_STRING")
CRYPTO_API_URL_ASSETS = os.getenv("CRYPTO_API_URL_ASSETS")
TIME_TO_SLEEP = int(os.getenv("REQUEST_DELAY"))

payload = {}
headers = {}

key_schema = avro.loads(KEY_SCHEMA_STRING)
value_schema = avro.load(SCHEMA_FILE)

producer_config = {
    "bootstrap.servers": BOOTSTRAP_SERVERS,
    "schema.registry.url": SCHEMA_REGISTRY,
}

producer = AvroProducer(
    producer_config, default_key_schema=key_schema, default_value_schema=value_schema
)


def main():
    response = requests.request(
        "GET", CRYPTO_API_URL_ASSETS, headers=headers, data=payload
    )

    status = response.status_code

    if response.status_code == 200:
        data = json.loads(response.text)["data"]
    else:
        print(f"Request Exception {status}")
        return

    data = [
        avro_value_schema_to_python_types(data_dic, value_schema) for data_dic in data
    ]

    try:
        for values in data:
            record_key = str(uuid.uuid4())
            producer.produce(topic=TOPIC, key=record_key, value=values)
    except Exception as e:
        print(
            f"Exception while producing record value - {values} to topic - {TOPIC}: {e}"
        )
    else:
        print(
            f"Successfully producing record values - count: {len(data)} to topic - {TOPIC}"
        )

    producer.flush()


if __name__ == "__main__":
    while True:
        main()
        sleep(TIME_TO_SLEEP)
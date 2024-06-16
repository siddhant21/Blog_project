from confluent_kafka import Consumer, KafkaError
from elasticsearch import Elasticsearch
import json

kafka_conf = {
    'bootstrap.servers': 'localhost:9092',
    'group.id': 'my-consumer-group',
    'auto.offset.reset': 'earliest'
}

es = Elasticsearch(['http://elasticsearch:9200'])

consumer = Consumer(kafka_conf)

consumer.subscribe(['blog-topic'])

while True:
    msg = consumer.poll(1.0)

    if msg is None:
        continue
    if msg.error():
        if msg.error().code() == KafkaError._PARTITION_EOF:
            continue
        else:
            print(msg.error())
            break

    message = json.loads(msg.value().decode('utf-8'))

    # Example: Index to Elasticsearch
    es.index(index='blogs', body=message)

consumer.close()


from math import prod
from kafka import KafkaProducer


bootstrap_server = ['localhost:29092']
topic = 'myTopic'

producer = KafkaProducer(bootstrap_servers=bootstrap_server)
for i in range(10):
    ack = producer.send('myTopic', f'Message number {i}'.encode())  # records should be encoded
    md = ack.get()
    print(f'Partition: {md.partition}, topic: {md.topic}')
producer.close()
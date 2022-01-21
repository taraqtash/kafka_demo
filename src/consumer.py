import sys

from kafka import KafkaConsumer


bootstrap_server = ['localhost:29092']
topicName = 'myTopic'
consumer = KafkaConsumer(topicName, 
                         group_id='group1',
                         bootstrap_servers=bootstrap_server,
                         auto_offset_reset='earliest')

try:
    for record in consumer:
        print(f'Record topic: {record.topic}\t'
                f'Record partition: {record.partition}\t'
                f'Record offset: {record.offset}\t'
                f'Record key: {record.key}\t'
                f'Record value: {record.value}')
except KeyboardInterrupt:
    sys.exit()

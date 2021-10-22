from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'jerry',
     bootstrap_servers=['localhost:9092'],
     auto_offset_reset='earliest',
     enable_auto_commit=True,
     group_id='my-group',
)

for message in consumer:
     print(message)

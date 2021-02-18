from kafka import KafkaConsumer
consumer = KafkaConsumer('sample', auto_offset_reset='earliest', group_id=None)
for message in consumer:
    print (message)
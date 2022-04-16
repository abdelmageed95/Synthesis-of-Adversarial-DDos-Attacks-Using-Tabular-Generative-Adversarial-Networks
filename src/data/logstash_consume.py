 
from kafka import KafkaConsumer

logstash_consumer = KafkaConsumer('GANs_raw_predictions', bootstrap_servers='localhost:9092', auto_offset_reset='earliest')
for msg in logstash_consumer:
    txt = msg.value.decode()
    print(txt)
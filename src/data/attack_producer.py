from kafka import KafkaProducer
import json
import numpy as np
TOPIC_NAME = "GANs_raw_predictions"



feature_names = ['Flow_ID','Source_Port' ,'Source_IP', 'Destination_IP','Bwd_Packet_Length Std', 'Destination_Port', 'Bwd_Packet_Length_Mean', 'Avg_Bwd_Segment_Size',
                 'Average_Packet_Size', 'Packet_Length_Variance', 'Packet_Length_Mean', 'Bwd_Packet_Length_Max',
                 'Init_Win_bytes_backward', 'Packet_Length_Std', 'predict','confidence_score']

def instantiate_kafka_producer():
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092',
    )
    
    if producer.bootstrap_connected():
        print(f"Successfully connected to bootstrap server")
    else:
        print("Couldn't connect to bootstrap server.")
        
    return producer

def produce_message(producer_instance, topic, message):
    producer_instance.send(topic, message)
    producer_instance.flush()
    return

def get_data(feature_names , positive_prediction):
    return {
        feature_names[0]:positive_prediction[0],
        feature_names[1]:positive_prediction[1],
        feature_names[2]:positive_prediction[2],
        feature_names[3]:positive_prediction[3].split("-")[0],
        feature_names[4]:np.float(positive_prediction[4]),
        feature_names[5]:np.float(positive_prediction[5]),
        feature_names[6]:np.float(positive_prediction[6]),
        feature_names[7]:np.float(positive_prediction[7]),
        feature_names[8]:np.float(positive_prediction[8]),
        feature_names[9]:np.float(positive_prediction[9]),
        feature_names[10]:np.float(positive_prediction[10]),
        feature_names[11]:np.float(positive_prediction[11]),
        feature_names[12]:np.float(positive_prediction[12]),
        feature_names[13]:np.float(positive_prediction[13]),
        feature_names[14]:np.float(positive_prediction[14]),
        feature_names[15]:np.float(positive_prediction[15])
    }


def send_attack_to_logstash(positive_prediction , producer) :
        #row = bytes(positive_prediction, encoding="utf-8")
        data = get_data(feature_names ,positive_prediction )
        row = json.dumps(data).encode('utf-8')
        produce_message(producer_instance=producer, topic=TOPIC_NAME, message=row)
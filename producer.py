import time 
import json 
import random 
from datetime import datetime
from data import generate_message
from kafka import KafkaProducer

# # membentuk pesannya ke data JSON 
# def serializer(message):
#     return json.dumps(message).encode('utf-8')

# Config kafka producer
producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    security_protocol="SASL_PLAINTEXT",
    sasl_mechanism="GSSAPI",
    sasl_kerberos_service_name="kafka",
    value_serializer=lambda v: json.dumps(v, separators=(",", ":")).encode(
        "utf-8"
    ),
    api_version=(0, 10, 1),
    batch_size=0,
)

#run produce kafka
if __name__ == '__main__':
    # membuat looping untuk send topic dan messagenya
    while True:
        # ngambil dari func di file data.py
        ex_message = generate_message()
        
        # sending topic and message 
        print(f'Producing message @ {datetime.now()} | Message = {str(ex_message)}')
        producer.send('messages', ex_message)
        
        # set time out nya
        time_to_sleep = random.randint(1, 11)
        time.sleep(time_to_sleep)
import json 
from kafka import KafkaConsumer

if __name__ == '__main__':
    # Kafka Consumer 
    consumer = KafkaConsumer(
        'messages',
        bootstrap_servers='localhost:9092',
        security_protocol="SASL_PLAINTEXT",
        sasl_mechanism="GSSAPI",
        sasl_kerberos_service_name="kafka",
        auto_offset_reset="latest",
        enable_auto_commit=True,
        # group_id="group-core-3",
    )
    for message in consumer:
        print(json.loads(message.value))
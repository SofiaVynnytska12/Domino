import json
import time
import uuid
from datetime import datetime
from kafka import KafkaProducer

# Настройки Kafka
KAFKA_TOPIC = "lottery_events"
KAFKA_SERVER = "localhost:9092"

# Инициализация Kafka Producer
producer = KafkaProducer(
    bootstrap_servers=KAFKA_SERVER,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

# Функция генерации событий
def generate_event():
    event = {
        "timestamp": datetime.utcnow().isoformat(),
        "uuid": str(uuid.uuid4()),
        "service_name": "lottery_system",
        "event_type": "ticket_purchased",
        "user_id": 1,
        "game_id": 101,
        "ticket_price": 100.00
    }
    return event

# Отправка события в Kafka
def send_event():
    event = generate_event()
    producer.send(KAFKA_TOPIC, value=event)
    producer.flush()
    print(f"Sent event: {event}")

if __name__ == "__main__":
    send_event()
    producer.close()

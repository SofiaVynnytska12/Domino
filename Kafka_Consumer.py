from confluent_kafka import Consumer
import json
import time


def main():
    # Consumer configuration
    config = {
        'bootstrap.servers': 'localhost:3306',  # Kafka broker address
        'group.id': '-',  # Consumer group ID
        'auto.offset.reset': 'earliest',
        'enable.auto.commit': True
    }

    consumer = Consumer(config)

    topic = 'test-topic'
    consumer.subscribe([topic])

    print(f"Starting Kafka consumer for topic: {topic}")
    print("Waiting for messages...")

    try:
        while True:
            msg = consumer.poll(1.0)

            if msg is None:
                continue

            if msg.error():
                print(f"Consumer error: {msg.error()}")
                continue

            key = msg.key().decode('utf-8') if msg.key() else None
            value = msg.value().decode('utf-8') if msg.value() else None

            print("Received message:")
            print(f"Partition: {msg.partition()}")
            print(f"Offset: {msg.offset()}")
            print(f"Key: {key}")

            try:
                json_data = json.loads(value)
                print(f"Value (JSON): {json.dumps(json_data, indent=2)}")

            except json.JSONDecodeError:
                print(f"Value (raw): {value}")

            print("-" * 50)

    except KeyboardInterrupt:
        print("Stopping consumer...")

    finally:
        consumer.close()
        print("Consumer closed")


if __name__ == "__main__":
    main()
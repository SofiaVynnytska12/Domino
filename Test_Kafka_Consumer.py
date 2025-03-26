import json
import os
from confluent_kafka import Consumer, Producer, KafkaError, KafkaException
from typing import List, Dict, Any, Optional


class ConfigurableKafkaConsumer:
    def __init__(self,
                 bootstrap_servers: str = 'localhost:9092',
                 topic: str = 'Domino',
                 group_id: str = 'Consumer_group'):
        """
        Налаштування Kafka Consumer з фільтрацією типів подій
        """
        # Дозволені типи подій з налаштувань
        self.enabled_event_types = self._get_enabled_event_types()

        # Налаштування підключення до Kafka
        self.consumer_config = {
            'bootstrap.servers': bootstrap_servers,
            'group.id': group_id,
            'auto.offset.reset': 'earliest'
        }

        # Створення споживача
        self.consumer = Consumer(self.consumer_config)

        # Підписка на топік
        self.consumer.subscribe([topic])

    def _get_enabled_event_types(self) -> List[str]:
        """
        Отримання дозволених типів подій з налаштувань
        """
        # За замовчуванням - всі типи подій
        event_types_str = os.getenv('ENABLED_EVENT_TYPES', '')
        return event_types_str.split(',') if event_types_str else []

    def _parse_message(self, msg) -> Optional[Dict[str, Any]]:
        """
        Розбір повідомлення з Kafka
        """
        try:
            # Декодування та парсинг JSON
            payload = msg.value().decode('utf-8')
            return json.loads(payload)
        except Exception as e:
            print(f"Помилка розбору повідомлення: {e}")
            return None

    def consume(self, timeout: float = 1.0):
        """
        Отримання повідомлень з топіку Kafka з фільтрацією
        """
        try:
            while True:
                msg = self.consumer.poll(timeout)

                if msg is None:
                    continue

                if msg.error():
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        print('Кінець розділу')
                    elif msg.error():
                        raise KafkaException(msg.error())
                    continue

                # Розбір повідомлення
                event = self._parse_message(msg)
                if not event:
                    continue

                # Тип події
                event_type = event.get('event_type')

                # Фільтрація повідомлень
                if not self.enabled_event_types or event_type in self.enabled_event_types:
                    print(f"Нове повідомлення:")
                    print(f"Ключ: {msg.key().decode('utf-8') if msg.key() else 'Без ключа'}")
                    print(f"Тип події: {event_type}")
                    print(f"Дані: {event}")
                    print("---")

        except KeyboardInterrupt:
            print("Споживач зупинений.")
        finally:
            self.consumer.close()


def create_kafka_topic(bootstrap_servers: str, topic: str):
    """
    Створення топіку в Kafka
    """
    from confluent_kafka.admin import AdminClient, NewTopic

    admin_client = AdminClient({'bootstrap.servers': bootstrap_servers})

    # Створення нового топіку
    new_topics = [NewTopic(topic, num_partitions=1, replication_factor=1)]

    # Створення топіків
    fs = admin_client.create_topics(new_topics)

    # Перевірка результату
    for topic, f in fs.items():
        try:
            f.result()
            print(f"Топік {topic} створено")
        except Exception as e:
            print(f"Помилка створення топіку {topic}: {e}")


def generate_test_data(bootstrap_servers: str, topic: str):
    """
    Генерація тестових повідомлень для Kafka
    """
    # Створення топіку
    create_kafka_topic(bootstrap_servers, topic)

    # Налаштування продюсера
    producer_config = {
        'bootstrap.servers': bootstrap_servers
    }
    producer = Producer(producer_config)

    # Тестові повідомлення
    test_messages = [
        ('user_1', {'event_type': 'user_login', 'username': 'john_doe'}),
        ('user_2', {'event_type': 'user_logout', 'username': 'jane_smith'}),
        ('order_1', {'event_type': 'order_created', 'order_id': '12345'}),
        ('order_2', {'event_type': 'payment_processed', 'order_id': '67890'})
    ]

    # Надсилання повідомлень
    for key, message in test_messages:
        producer.produce(
            topic,
            key=key.encode('utf-8'),
            value=json.dumps(message).encode('utf-8')
        )

    # Очікування надсилання
    producer.flush()
    print("Тестові дані надіслано.")


def main():
    # Параметри підключення
    bootstrap_servers = 'localhost:9092'
    topic = 'Domino'

    # Генерація тестових даних
    generate_test_data(bootstrap_servers, topic)

    # Створення та запуск споживача
    consumer = ConfigurableKafkaConsumer(
        bootstrap_servers=bootstrap_servers,
        topic=topic,
        group_id='Сonsumer_group'
    )
    consumer.consume()


if __name__ == '__main__':
    main()
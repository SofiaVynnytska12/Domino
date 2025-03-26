import json
import os
from confluent_kafka import Consumer, KafkaError, KafkaException
from typing import List, Dict, Any, Optional


class SimpleKafkaConsumer:
    def __init__(self,
                 bootstrap_servers: str = 'localhost:9092',
                 topic: str = 'Domino'):
        """
        Настройка Kafka Consumer для подключения к существующему топику
        """
        # Настройки подключения к Kafka
        self.consumer_config = {
            'bootstrap.servers': bootstrap_servers,
            'auto.offset.reset': 'earliest'  # Начать с самых ранних сообщений
        }

        # Создание консьюмера
        self.consumer = Consumer(self.consumer_config)

        # Подписка на топик
        self.consumer.subscribe([topic])

    def _parse_message(self, msg) -> Optional[Dict[str, Any]]:
        """
        Разбор сообщения из Kafka
        """
        try:
            # Декодирование и парсинг JSON
            payload = msg.value().decode('utf-8')
            return json.loads(payload)
        except Exception as e:
            print(f"Ошибка разбора сообщения: {e}")
            return None

    def consume(self,
                timeout: float = 1.0,
                max_messages: int = None):
        """
        Получение сообщений из топика Kafka

        :param timeout: Время ожидания сообщений
        :param max_messages: Максимальное количество сообщений для получения
        """
        message_count = 0

        try:
            while True:
                # Если указано максимальное количество сообщений и оно достигнуто
                if max_messages is not None and message_count >= max_messages:
                    break

                # Получение сообщения
                msg = self.consumer.poll(timeout)

                if msg is None:
                    # Если нет сообщений, продолжаем
                    print("Нет новых сообщений.")
                    break

                if msg.error():
                    # Обработка ошибок Kafka
                    if msg.error().code() == KafkaError._PARTITION_EOF:
                        print('Достигнут конец раздела')
                        break
                    elif msg.error():
                        raise KafkaException(msg.error())

                # Разбор сообщения
                event = self._parse_message(msg)
                if not event:
                    continue

                # Вывод информации о сообщении
                print(f"Новое сообщение:")
                print(f"Ключ: {msg.key().decode('utf-8') if msg.key() else 'Без ключа'}")
                print(f"Данные: {event}")
                print("---")

                message_count += 1

        except KeyboardInterrupt:
            print("Потребитель остановлен пользователем.")
        finally:
            # Закрытие соединения
            self.consumer.close()


def main():
    # Параметры подключения
    bootstrap_servers = 'localhost:9092'
    topic = 'Domino'

    # Создание и запуск консьюмера
    consumer = SimpleKafkaConsumer(
        bootstrap_servers=bootstrap_servers,
        topic=topic
    )

    # Получение сообщений (например, максимум 10)
    consumer.consume(max_messages=10)


if __name__ == '__main__':
    main()
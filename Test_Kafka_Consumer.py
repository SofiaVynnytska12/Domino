from confluent_kafka import Producer
import json


class KafkaProducer:
    def __init__(self, bootstrap_servers='localhost:9092'):
        """
        Инициализация продюсера Kafka
        """
        self.producer = Producer({
            'bootstrap.servers': bootstrap_servers
        })

    def send_message(self, topic, key, message):
        """
        Отправка сообщения в топик

        :param topic: название топика
        :param key: ключ сообщения
        :param message: словарь с сообщением
        """
        try:
            # Сериализация сообщения в JSON
            value = json.dumps(message).encode('utf-8')

            # Отправка сообщения с коллбэком доставки
            self.producer.produce(
                topic,
                key=key.encode('utf-8'),
                value=value,
                callback=self.delivery_report
            )

            # Принудительная отправка
            self.producer.flush()
        except Exception as e:
            print(f"Ошибка при отправке сообщения: {e}")

    def delivery_report(self, err, msg):
        """
        Callback для проверки доставки сообщения
        """
        if err is not None:
            print(f'Ошибка доставки: {err}')
        else:
            print(f'Сообщение доставлено в {msg.topic()} [{msg.partition()}]')


def main():
    # Создание продюсера
    producer = KafkaProducer()

    # Отправка тестового сообщения
    producer.send_message(
        topic='Domino',
        key='user_123',
        message={
            'event_type': 'user_login',
            'username': 'john_doe'
        }
    )


if __name__ == '__main__':
    main()
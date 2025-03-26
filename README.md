Назва команди: Domino

Учасники: 
Чернецький Андрій(a4era)
Василенко Олександр(JunkaD)
Костюк Кирило(RaspBerry43)
Дейнека Володимир(Kormonal)

1.Назва проекту

Lottery Data Analysis – Аналіз дій користувачів у веб-додатку «Лотерея».

2.Опис проекту

Проект аналізує дії користувачів у веб-додатку «Лотерея», включаючи статистику реєстрацій, виграшів, таблицю лідерів та загальну суму отриманих коштів. Дані зберігаються у базі даних MySQL, а аналіз виконується за допомогою Python.

3.Використовувані технології
Python version 3.13
PyCharm Community Edition 2024.3.3
Бібліотеки: --

MySql Workbench 8.0 CE;
test connection (localhost:3306)

Docker Desktop 4.38.0
ports:  
"9092:9092"
"29092:29092" # Для внутрішнього з'єднання


# Kafka Lottery Event Publisher
Этот проект предназначен для генерации и отправки событий в Apache Kafka.

## 1. Структура проекта
```
my_project\publisher
│── docker-compose.yml  # Запуск Kafka в KRaft Mode
│── producer.py         # Генерация и отправка событий в Kafka
│── scheduler.py        # Запуск producer.py через subprocess
│── config.json         # Конфигурация Kafka
│── mock_data.py        # Генерация мокированных данных
│── README.md           # Документация проекта
```

## 2. Установка и запуск Kafka
1. Убедитесь, что у вас установлен [Docker](https://www.docker.com/).
2. Запустите Kafka в режиме KRaft с помощью:
   ```sh
   docker-compose up -d
   ```
3. Убедитесь, что Kafka работает:
   ```sh
   docker ps
   ```

## 3. Запуск producer.py вручную
```sh
python producer.py
```

## 4. Автоматический запуск producer.py
python scheduler.py


2. Убедитесь, что producer.py автоматически отправляет события в Kafka.

## 5. Проверка событий в Kafka
Запустите команду:
```sh
docker exec -it kafka_kraft kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic lottery_events --from-beginning
```

Вы должны увидеть события в реальном времени.


Назва команди: Domino

Учасники: Чернецький Андрій(a4era) Василенко Олександр(JunkaD) Костюк Кирило(RaspBerry43) Дейнека Володимир(Kormonal)

1.Назва проекту

Lottery Data Analysis – Аналіз дій користувачів у веб-додатку «Лотерея».

2.Опис проекту

Проект аналізує дії користувачів у веб-додатку «Лотерея», включаючи статистику реєстрацій, виграшів, таблицю лідерів та загальну суму отриманих коштів. Дані зберігаються у базі даних MySQL, а аналіз виконується за допомогою Python.

3.Використовувані технології Python version 3.13 PyCharm Community Edition 2024.3.3 Бібліотеки: --

MySql Workbench 8.0 CE; test connection (localhost:3306)

Docker Desktop 4.38.0 ports:
"9092:9092" "29092:29092" # Для внутрішнього з'єднання




### Этот проект предназначен для развертывания MySQL-сервера в контейнере Docker с использованием `docker-compose`.  
## 1. Структура проекта  
```
my_mysql_project
│── docker-compose.yml  # Файл для запуска MySQL в Docker
│── .env                # Конфигурация MySQL (переменные окружения)
│── README.md           # Документация проекта
```

---

## 2. Установка и запуск MySQL  
### **1. Убедитесь, что установлен Docker**  
Если Docker ещё не установлен, скачайте его с [официального сайта](https://www.docker.com/products/docker-desktop).  

### **2. Создайте `.env` файл с настройками**  
Файл `.env` содержит конфигурацию для MySQL (пароли, логины и базу данных).  

Пример содержимого файла `.env`:  
```
MYSQL_ROOT_PASSWORD=supersecret
MYSQL_DATABASE=mydatabase
MYSQL_USER=myuser
MYSQL_PASSWORD=mypassword
```

### **3. Запустите MySQL в контейнере**  
Выполните команду:  
```sh
docker-compose up -d
```  
Это создаст и запустит контейнер с MySQL.  

### **4. Проверьте, что MySQL запущен**  
```sh
docker ps
```
Если контейнер `mysql_container` в списке — значит, сервер работает.  

---

## 3. Подключение к MySQL  
### 🔹 **Через командную строку (CLI)**  
Запустите:  
```sh
docker exec -it mysql_container mysql -u root -p
```
Введите пароль `supersecret` (или тот, что указан в `.env`).  

Проверим базы данных:  
```sql
SHOW DATABASES;
```

### 🔹 **Через MySQL Workbench / DBeaver**  
Подключение через GUI-клиент:  
- **Host:** `localhost`
- **Port:** `3306`
- **User:** `myuser`
- **Password:** `mypassword`
- **Database:** `mydatabase`

---

## 4. Остановка и удаление контейнера  
Чтобы остановить MySQL, выполните команду:  
```sh
docker-compose down
```  
Если нужно удалить все данные:  
```sh
docker-compose down -v
```  

---

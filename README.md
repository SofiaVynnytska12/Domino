Этот проект предназначен для развертывания MySQL-сервера в контейнере Docker с использованием `docker-compose`.  

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

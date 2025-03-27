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

Хід виконання DOM-7 Add migrations for DB schema creation:
1. Встановлення Liquibase
2. Створення структури проєкту
В папці my_creations/ створюємо файли міграцій:
my_creations/
  ├── 001_create_users_table.yaml
  ├── 002_create_games_table.yaml
  ├── 003_create_tickets_table.yaml
  ├── 004_create_results_table.yaml
  ├── 005_create_winnings_table.yaml
  ├── README.md
  ├── changelog.yaml   <-- (тут буде головний файл змін)
3. Створення changelog.yaml
У файлі changelog.yaml потрібно оголосити всі міграції:
databaseChangeLog:
  - changeSet:
      id: "001"
      author: "kormonal"
      changes:
        - include:
            file: my_creations/001_create_users_table.yaml
        - include:
            file: my_creations/002_create_games_table.yaml
        - include:
            file: my_creations/003_create_tickets_table.yaml
        - include:
            file: my_creations/004_create_results_table.yaml
        - include:
            file: my_creations/005_create_winnings_table.yaml
4. Створення файлуц конфігурації 
Файл конфігурації liquibase.properties.
5. Запуск перевірки (без внесення змін)
Перед тим як оновлювати БД, перевіримо, чи все працює:
Команда: liquibase validate
6. Виконання міграцій
Запускаємо оновлення схеми бази:
Команда: liquibase update


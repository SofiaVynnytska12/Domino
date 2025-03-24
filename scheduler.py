import subprocess
import time

while True:
    print("Запуск producer.py...")
    subprocess.run(["python", "producer.py"], check=True)
    print("Ожидание 60 секунд перед следующим запуском...")
    time.sleep(60)

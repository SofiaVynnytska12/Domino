import random
import uuid
from datetime import datetime

# Функция генерации случайного пользователя
def generate_user():
    return {
        "user_id": random.randint(1, 1000),
        "username": f"user_{random.randint(1000, 9999)}",
        "email": f"user{random.randint(1000, 9999)}@example.com",
        "registration_date": datetime.utcnow().isoformat()
    }

# Функция генерации случайной игры
def generate_game():
    games = [
        {"game_id": 101, "game_name": "MegaLotto", "game_type": "Numeric Lottery", "ticket_price": 10.00, "max_prize": 1000000.00},
        {"game_id": 102, "game_name": "Quick Jackpot", "game_type": "Instant Lottery", "ticket_price": 5.00, "max_prize": 50000.00}
    ]
    return random.choice(games)

# Функция генерации случайного билета
def generate_ticket(user_id, game_id):
    return {
        "ticket_id": uuid.uuid4().hex[:8],
        "user_id": user_id,
        "game_id": game_id,
        "purchase_date": datetime.utcnow().isoformat(),
        "ticket_numbers": ",".join(str(random.randint(1, 50)) for _ in range(5))
    }

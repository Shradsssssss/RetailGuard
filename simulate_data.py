import random
import pandas as pd

def generate_user_data(num_users=100):
    data = []

    for _ in range(num_users):
        is_bot = random.random() < 0.2  # 20% chance of being a bot
        session_time = random.gauss(300, 100) if not is_bot else random.gauss(30, 10)
        clicks = random.randint(5, 20) if not is_bot else random.randint(40, 100)
        added_to_cart = random.randint(0, 3) if not is_bot else random.randint(10, 30)
        reviews_written = 0 if not is_bot else random.randint(5, 20)

        data.append({
            "session_time": max(10, int(session_time)),
            "clicks": clicks,
            "cart_adds": added_to_cart,
            "reviews": reviews_written,
            "label": 1 if is_bot else 0  # 1 = bot, 0 = human
        })

    df = pd.DataFrame(data)
    df.to_csv("user_sessions.csv", index=False)
    print("✅ user_sessions.csv generated with", len(df), "rows")

generate_user_data()

import os

# os.environ — це словник, де Python зберігає всі змінні системи
print(f"Значення змінної IT_TEST = {os.environ.get('IT_TEST')}")
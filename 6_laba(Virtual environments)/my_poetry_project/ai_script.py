import requests

def get_fact():
    print("--- Цікавий факт від AI ---")
    try:
        # Отримуємо випадковий факт про котів (це найпростіший API)
        response = requests.get("https://catfact.ninja/fact")
        if response.status_code == 200:
            fact = response.json()['fact']
            print(f"Факт дня: {fact}")
        else:
            print("Не вдалося отримати дані.")
    except Exception as e:
        print(f"Помилка: {e}")

if __name__ == "__main__":
    get_fact()
from flask import Flask
from jikanpy import Jikan

# Ініціалізація API та Flask
jikan = Jikan()
app = Flask(__name__)

# Отримуємо дані про аніме (ID 54595 — це "Frieren")
j = jikan.anime(54595, extension='episodes')


@app.route('/')
def home():
    a = ""
    # Цикл проходить по всіх епізодах
    for episode in j["data"]:
        # Розбиваємо довгий рядок на два, щоб прибрати помилку E501
        a += (
            f"<p>Епізод {episode['mal_id']} з назвою: {episode['title']} "
            f"має оцінку {episode['score']}</p>"
        )

    return a


if __name__ == '__main__':
    app.run(debug=True)

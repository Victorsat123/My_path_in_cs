import os
from abc import ABC, abstractmethod
from typing import Optional
from dotenv import load_dotenv

# Імпортуємо базовий клас для створення агента з бібліотеки курсу
from google.adk import Agent

# Завантажуємо секретний API-ключ з файлу .env, щоб агент міг працювати
load_dotenv()

# =====================================================================
# ЧАСТИНА 1: ООП-КЛАСИ (Реалізація 4 парадигм)
# =====================================================================

# 1. ПАРАДИГМА: АБСТРАКЦІЯ
class LibraryItem(ABC):
    def __init__(self, title: str, year: int):
        self.title = title
        self.year = year

    # @abstractmethod змушує всі дочірні класи реалізувати цю функцію
    @abstractmethod
    def get_info(self) -> dict:
        pass


# 2. ПАРАДИГМА: НАСЛІДУВАННЯ
# Клас "Книга" бере всі властивості від LibraryItem (назву і рік) 
# і додає свої унікальні (автора та кількість сторінок).
class Book(LibraryItem):
    def __init__(self, title: str, year: int, author: str, pages: int):
        super().__init__(title, year) # Викликаємо ініціалізацію батька
        self.author = author
        self.pages = pages

    # Реалізуємо абстрактний метод для конкретної книги
    def get_info(self) -> dict:
        return {
            "type": "Книга",
            "title": self.title,
            "year": self.year,
            "author": self.author,
            "pages": self.pages
        }


# НАСЛІДУВАННЯ (Продовження)
# Клас "Журнал" також бере базу від LibraryItem, але додає номер і тему.
class Magazine(LibraryItem):
    def __init__(self, title: str, year: int, issue: int, topic: str):
        super().__init__(title, year)
        self.issue = issue
        self.topic = topic

    def get_info(self) -> dict:
        return {
            "type": "Журнал",
            "title": self.title,
            "year": self.year,
            "issue": self.issue,
            "topic": self.topic
        }


class Library:
    def __init__(self):
        # 3. ПАРАДИГМА: ІНКАПСУЛЯЦІЯ
        # Подвійне підкреслення (__) робить список приватним.
        # Ніхто не зможе змінити каталог напряму ззовні, тільки через метод add().
        self.__catalog = []

    # Метод для додавання елементів у приватний каталог
    def add(self, item: LibraryItem):
        self.__catalog.append(item)

    # Метод для пошуку елемента за назвою (без урахування регістру)
    def find(self, title: str) -> Optional[LibraryItem]:
        for item in self.__catalog:
            if item.title.lower() == title.lower():
                return item
        return None

    def list_all(self):
        # 4. ПАРАДИГМА: ПОЛІМОРФІЗМ
        # Ми просто викликаємо .get_info() для кожного елемента.
        # Програма сама розуміє, який саме get_info виконати: 
        # для книги він поверне автора, а для журналу — номер випуску.
        return [item.get_info() for item in self.__catalog]


# =====================================================================
# ЧАСТИНА 2: ІНСТРУМЕНТ (TOOL) ДЛЯ АГЕНТА
# =====================================================================

def search_book(title: str) -> dict:
    """
    Цей опис (докстрінг) дуже важливий — ШІ читає його, щоб зрозуміти, 
    коли і як використовувати цей інструмент.
    Шукає книгу або журнал за назвою в бібліотечному каталозі.
    Повертає інформацію про видання або {"found": False}, якщо не знайдено.
    """
    library = Library()
    
    # Наповнюємо нашу віртуальну бібліотеку тестовими даними
    library.add(Book("1984", 1949, "Джордж Оруелл", 328))
    library.add(Book("Кобзар", 1840, "Тарас Шевченко", 700))
    library.add(Magazine("National Geographic", 2023, 10, "Природа"))
    library.add(Magazine("Forbes", 2024, 1, "Бізнес та фінанси"))

    item = library.find(title)
    if item:
        return item.get_info()
    
    return {"found": False}


# =====================================================================
# ЧАСТИНА 3: СТВОРЕННЯ AI-АГЕНТА
# =====================================================================

# ВАЖЛИВО: Назва змінної має бути саме root_agent, щоб працювала команда 'adk web .'
root_agent = Agent(
    name="library_assistant",
    model="gemini-3.5-flash", # Актуальна модель, яка працює без помилок 404
    instruction=(
        "Ти є бібліотечним помічником. Ти шукаєш книги та журнали "
        "за назвою (використовуючи доступний інструмент search_book) та надаєш "
        "інформацію про них. Відповідай українською мовою ввічливо та зрозуміло."
    ),
    tools=[search_book] # Передаємо нашу функцію як інструмент
)


# Цей блок потрібен для перевірки коду через консоль (якщо запустити python agent.py)
if __name__ == "__main__":
    print("🚀 Запуск демонстрації агента в консолі...\n")
    queries = [
        "Розкажи мені, чи є у вас книга '1984' і хто її автор?",
        "Мене цікавить журнал 'Forbes'. Який випуск та тема у вас є?",
        "Чи є в бібліотеці книга 'Володар перснів'?"
    ]

    for q in queries:
        print(f"👤 Користувач: {q}")
        response = root_agent.run(q)
        print(f"🤖 Агент: {response}\n")
        print("-" * 50 + "\n")
#Приклад_1
# Список слів
words = ["apple", "banana", "avocado", "blueberry", "cherry", "grape"]

# Лямбда-функція для пошуку слів, що починаються з заданої букви
find_words_starting_with = lambda char: [word for word in words if word.startswith(char)]

# Тестуємо лямбду
search_char = "b"  # Ти можеш змінити на будь-яку букву
filtered_words = find_words_starting_with(search_char)

# Виводимо результат
print(f"Слова, що починаються на '{search_char}':", filtered_words)




#Приклад_2
# Список людей з віком
people = [
    {"name": "Orest", "age": 17},
    {"name": "Victor", "age": 17},
    {"name": "Yaroslaw", "age": 18},
    {"name": "Maria", "age": 16}
]

# Сортуємо за віком
sorted_people = sorted(people, key=lambda person: person["age"])

# Вивести відсортований список
print(sorted_people)

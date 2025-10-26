# Приклад 1:
# Користувацький ввід
user_input = input("Введіть число: ")

try:
    # Спроба перетворити рядок в число
    number = int(user_input)
    print(f"Ви ввели число: {number}")
except ValueError as e:
    # Обробка помилки, якщо введено не число
    print("Помилка! Ви ввели не числове значення:", e)
except Exception as e:
    # Обробка інших помилок
    print("Сталася непередбачена помилка:", e)
finally:
    print("Програма завершена. Дякуємо за використання!")



# Приклад 2:
try:
    # Спроба відкрити неіснуючий файл
    file = open("not_existing_file.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError as e:
    # Обробка помилки, якщо файл не знайдено
    print("Помилка! Файл не знайдено:", e)
except Exception as e:
    # Обробка інших помилок
    print("Сталася непередбачена помилка:", e)
finally:
    try:
        file.close()  # Закриття файлу
        print("Файл закрито.")
    except NameError:
        print("Файл не був відкритий, тому не можна закрити.")

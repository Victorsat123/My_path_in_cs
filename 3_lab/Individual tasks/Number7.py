class MyName:
    """Опис класу / Документація"""
    total_names = 0  # Class Variable

    def __init__(self, name=None) -> None:
        """Ініціалізація класу"""
        raw_name = name if name is not None else self.anonymous_user().name
        clean_name = raw_name.capitalize()  # Перша літера велика

        # ----------- ДОДАНО ПЕРЕВІРКУ -----------
        if not clean_name.isalpha():  # Перевіряє, що всі символи - літери
            raise ValueError("Ім'я може містити лише літери!")
        # -----------------------------------------

        self.name = clean_name
        MyName.total_names += 1
        self.my_id = MyName.total_names

    @property
    def whoami(self) -> str:
        return f"My name is {self.name}"

    @property
    def my_email(self) -> str:
        return self.create_email()

    def create_email(self, domain: str = "itcollege.lviv.ua") -> str:
        """Повертає email з можливістю змінити домен"""
        return f"{self.name}@{domain}"

    @classmethod
    def anonymous_user(cls):
        return cls("Anonymous")

    @staticmethod
    def say_hello(message="Hello to everyone!") -> str:
        return f"You say: {message}"

    def name_length(self) -> int:
        return len(self.name)


print("Розпочинаємо створювати обєкти!")

names = ("Bohdan", "Marta", None, "Victor5242323")  # останнє ім'я викличе помилку
all_names = {}

for name in names:
    try:
        all_names[name] = MyName(name)
    except ValueError as e:
        print(f"Помилка при створенні об'єкта з ім'ям '{name}': {e}")

# Підрахунок елементів у списку names
print(f"\nNumber of elements in names list: {len(names)}\n")

for name, me in all_names.items():
    print(f"""{">*<"*20}
This is object: {me} 
This is object attribute: {me.name} / {me.my_id}
This is {type(MyName.whoami)}: {me.whoami} / {me.my_email}
This is {type(me.create_email)} call with gmail.com: {me.create_email("gmail.com")}
This is static {type(MyName.say_hello)} with defaults: {me.say_hello()} 
This is class variable {type(MyName.total_names)}: from class {MyName.total_names} / from object {me.total_names}
This name has {me.name_length()} letters
{"<*>"*20}""")

print(f"\nWe are done. We create {len(all_names)} valid names! ??? Why {MyName.total_names}?")

class MyName:
    """Опис класу / Документація"""
    total_names = 0  # Class Variable

    def __init__(self, name=None) -> None:
        """Ініціалізація класу"""
        raw_name = name if name is not None else self.anonymous_user().name
        self.name = raw_name.capitalize()  # Перша літера велика
        MyName.total_names += 1
        self.my_id = MyName.total_names

    @property
    def whoami(self) -> str:
        return f"My name is {self.name}"

    @property
    def my_email(self) -> str:
        # Виклик create_email без аргументів → стандартний домен
        return self.create_email()

    # ----------- МОДИФІКОВАНО -----------
    def create_email(self, domain: str = "gmail.com") -> str:
        """Повертає email з можливістю змінити домен"""
        return f"{self.name}@{domain}"
    # -------------------------------------

    @classmethod
    def anonymous_user(cls):
        return cls("Anonymous")

    @staticmethod
    def say_hello(message="Hello to everyone!") -> str:
        return f"You say: {message}"

    def name_length(self) -> int:
        return len(self.name)


print("Розпочинаємо створювати обєкти!")

names = ("Bohdan", "Marta", None)
all_names = {name: MyName(name) for name in names}

# Підрахунок елементів у списку names
print(f"Number of elements in names list: {len(names)}\n")

for name, me in all_names.items():
    print(f"""{">*<"*20}
This is object: {me} 
This is object attribute: {me.name} / {me.my_id}
This is {type(MyName.whoami)}: {me.whoami} / {me.my_email}
# Виклик create_email з іншим доменом
This is {type(me.create_email)} call with gmail.com: {me.create_email("gmail.com")}
This is static {type(MyName.say_hello)} with defaults: {me.say_hello()} 
This is class variable {type(MyName.total_names)}: from class {MyName.total_names} / from object {me.total_names}
This name has {me.name_length()} letters
{"<*>"*20}""")

print(f"\nWe are done. We create {me.total_names} names! ??? Why {MyName.total_names}?")

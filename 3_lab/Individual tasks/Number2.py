class MyName:
    """Опис класу / Документація"""
    total_names = 0  # Class Variable

    def __init__(self, name=None) -> None:
        """Ініціалізація класу"""
        self.name = name if name is not None else self.anonymous_user().name  # Class attributes / Instance variables
        MyName.total_names += 1  # modify class variable
        self.my_id = self.total_names

    @property
    def whoami(self) -> str:
        """Class property"""
        return f"My name is {self.name}"

    @property
    def my_email(self) -> str:
        """Class property"""
        return self.create_email()

    def create_email(self) -> str:
        """Instance method"""
        return f"{self.name}@itcollege.lviv.ua"

    @classmethod
    def anonymous_user(cls):
        """Classs method"""
        return cls("Anonymous")

    def say_hello(self, message="Hello to everyone!") -> str:
        """Instance method"""
        return f"You say: {message}"

# Тепер викликаємо метод say_hello для конкретного екземпляра:
bohdan = MyName("Bohdan")
print(bohdan.say_hello("Hi, I'm Bohdan!"))

marta = MyName("Marta")
print(marta.say_hello("Greetings from Marta!"))
# Создаем родительский класс Bird/Птица
class Bird():
    # Создаём характеристики объекта
    def __init__(self, name, voice, color):
        self.name = name
        self.voice = voice
        self.color = color

    # Созадём функции объекта
    def fly(self):
        print(f"{self.name} летает")

    def eat(self):
        print(f"{self.name} кушает")

    def sing(self):
        print(f"{self.name} поёт - {self.voice}")

    def info(self):
        print(f"{self.name} - имя")
        print(f"{self.voice} - голос")
        print(f"{self.color} - окрас птицы")

# Создаем дочерний класс Pigeon/Голубь
class Pigeon(Bird):
    def __init__(self, name, voice, color, favourite_food):
        # Берем характеристики из родительского класса
        super().__init__(name, voice, color)
        # Добавляем новые характеристики дочернего класса
        self.favourite_food = favourite_food

    # Добавляем новый метод дочернего класса
    def walk(self):
        print(f"{self.name} гуляет")

bird1 = Pigeon("Гоша", "курлык-курлык", "сизый", "пшено")

bird1.sing()
bird1.info()
bird1.walk()

bird2 = Bird("Ворона", "кар-кар", "серая")
bird2.info()


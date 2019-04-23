# Добавить в класс Pet пустой метод voice. Заменить имена методов bark, meow на voice.
# Создать функцию, принимающая список животных и вызывающая у каждого животного метод voice.
class Pet:
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    def voice(self):
        pass


class Dog(Pet):
    def voice(self):
        print('gav gav')


class Cat(Pet):
    def voice(self):
        print('mewo mewo')


def call_voice(pets):
    for pet in pets:
        pet.voice()


pets = [Dog('Rony', 10, 'Max', 10), Cat('Maksim', 2, 'Ilya', 12)]
call_voice(pets)

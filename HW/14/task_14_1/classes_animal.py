from abc import abstractmethod


class Animal:
    @abstractmethod
    def voice(self):
        pass

    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight


class Pet(Animal):
    pass


class WildAnimal(Animal):
    pass


class FelineInterface():
    @abstractmethod
    def climb(self):
        print('climbing')

    pass


class CanineInterface():
    @abstractmethod
    def growl(self):
        print('growling')

    pass


class Dog(Pet, FelineInterface):
    def voice(self):
        print('gau gau')

    def growl(self):
        print('growling')


class Cat(Pet, CanineInterface):
    def voice(self):
        print('myau myau')

    def climb(self):
        print('climbing')


class Lion(WildAnimal, CanineInterface):
    def voice(self):
        print('af af')

    def climb(self):
        print('climbing')


class Wolf(WildAnimal, FelineInterface):
    def voice(self):
        print('woof woof')

    def growl(self):
        print('growling')
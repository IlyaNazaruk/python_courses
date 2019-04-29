from classes_animal import Dog, Lion, Cat, Wolf


def create_dog():
    return Dog('max', 3, 42, 12)

def create_wolf():
    return Wolf('dron', 2, 90, 28)

def create_cat():
    return Cat('timoxa', 2, 6, 8)

def create_lion():
    return Lion('simba', 5, 120, 40)


def call_voice(*animals):
    for animal in animals:
        animal.voice()


def call_climb(*cats):
    for cat in cats:
        cat.climb()


def call_growl(*dogs):
    for dog in dogs:
        dog.growl()
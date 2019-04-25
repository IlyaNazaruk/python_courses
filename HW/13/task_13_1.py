from task_13_1_1 import (
    Pet,
    Cat,
    Dog,
    Parrot,
    Horse,
    Donkey,
    Mule
)
horse = Horse("pqly", 5, "opq", 12, 100)
donkey = Donkey("Fredy", 5, "zal", 51, 1500)
mule = Mule("pqa", 5, "plq", 50, 150)
cat = Cat("Fridrih", 5, "Liza", 50, 1500)
print(cat.name)
print(cat.master)
cat.voice()
cat.birthday()
print(cat.age)

dog = Dog("Ilya", 12, "Max", 70, 3000)
print(dog.name)
print(dog.master)
dog.voice()
dog.birthday()
dog.birthday()
dog.birthday()
dog.birthday()
dog.birthday()
print(dog.age)
dog.is_alive
dog.change_weight()
print(dog.weight)

parrot = Parrot("Kesha", 3, "Bob", 10, 200, 'orange')
print(parrot.name)
print(parrot.master)
parrot.fly()
parrot.birthday()
parrot.change_weight()
print(parrot.weight)
print(parrot.age)
parrot.fly()
print(parrot.species)
print(Pet.get_counter())
mule.voice()
print(Pet.get_random_name())
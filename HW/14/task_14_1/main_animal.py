from func_animal import create_dog, create_wolf, create_lion, create_cat, \
    call_voice, call_climb, call_growl

dog = create_dog()
wolf = create_wolf()
cat = create_cat()
lion = create_lion()
call_voice(dog, wolf, cat, lion)
call_climb(cat, lion)
call_growl(dog, wolf)
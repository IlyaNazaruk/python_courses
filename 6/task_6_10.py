# Написать игру. Пользователь должен угадать число. Сперва вводиться диапазон угадывания.
# После колличество попыток. В случае правильного ответа - выводить You are the winner.
# В случае неправильного давать игроку подсказку(больше или меньше искомое число).
# Если за указанное количество попыток число не угадано - выводить: You are the loser и правильное число.
start = int(input('enter the start '))
finish = int(input('enter the finish '))
number_of_attempts = int(input('enter the numbers of attempts '))
import random
random_number = int(random.randint(start, finish))
print(random_number)
for attempt in range(number_of_attempts):
    my_number = int(input('what is your number? '))
    if my_number == random_number:
        print('You are the winner')
        break
    elif my_number < random_number:
        if attempt + 1 == number_of_attempts:
            print('u are looser this number is -', random_number)
            break
        else:
            print('your number <<<< than')
    elif my_number > random_number:
        if attempt + 1 == number_of_attempts:
            print('u are looser this number is -', random_number)
            break
        else:
            print('your number >>>>>> than')
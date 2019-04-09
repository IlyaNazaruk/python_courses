# Дано число. Найти сумму и произведение его цифр.
number = input('enter the number')
list_of_numbers = []
len_number = len(number)
sum = 0
product = 1
while len_number != 0:
    sum += int(number[len_number - 1])
    product *= int(number[len_number - 1])
    len_number -= 1
print(sum, product)
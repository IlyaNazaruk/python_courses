
# Для каждого натурального числа в промежутке от m до n вывести все делители,
# кроме единицы и самого числа. m и n вводятся с клавиатуры.
# Пример:m =100, n = 105
# 100: 2 4 5 10 20 25 50
# 101:
# 102: 2 3 6 17 34 51
# 103:
# 104: 2 4 8 13 26 52
# 105: 3 5 7 15 21 35
left = int(input())
right = int(input())
counter = 2
raw_of_numbers=[2]
coun1 = 2
# while coun1 != n:
#     raw_of_numbers.append(coun1+1)
#     coun1 +=1
for coun1 in range (coun1, right):
    raw_of_numbers.append(coun1+1)
i = 1
for left in range(left, right+1):
    print(left,':', end=' ')
    for counter in range(counter,right-1):
        for i in range(right-1):
          if left / counter == raw_of_numbers[i] :
              print(counter, end=' ')
    counter = 2
    i = 1
    print()

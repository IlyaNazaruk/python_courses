
# Для каждого натурального числа в промежутке от m до n вывести все делители,
# кроме единицы и самого числа. m и n вводятся с клавиатуры.
# Пример:m =100, n = 105
# 100: 2 4 5 10 20 25 50
# 101:
# 102: 2 3 6 17 34 51
# 103:
# 104: 2 4 8 13 26 52
# 105: 3 5 7 15 21 35
m = int(input())
n = int(input())
counter = 2
list=[2]
coun1 = 2
while coun1 != n:
    list.append(coun1+1)
    coun1 +=1
i = 1
for m in range(m, n+1):
    print(m,':', end=' ')
    for counter in range(counter,n-1):
        for i in range(n-1):
          if m / counter == list[i] :
              print(counter, end=' ')
    counter = 2
    i = 1
    print()

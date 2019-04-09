# Для заданного числа N составьте программу вычисления суммы
# S=1+1/2+1/3+1/4+...+1/N, где N – натуральное число. [02-3.2-ML21]
N = int(input('enter the number '))
counter = 1
sent = '1 +'
while counter != N:
    counter += 1
    sent = sent + ' 1 / ' + str(counter)
    if counter == N :
        break
    else:
        sent += ' +'
print(sent)
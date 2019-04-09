# Написать программу, в которой вводятся два операнда Х и Y и знак операции sign (+, –, /, *).
# Вычислить результат Z в зависимости от знака. Предусмотреть реакции на возможный неверный знак операции,
# а также на ввод Y=0 при делении. Организовать возможность многократных вычислений без перезагрузки программа
# (т.е. построить бесконечный цикл). В качестве символа прекращения вычислений принять ‘0’ (т.е. sign='0').
sign = 1
while sign != '0':
 X = int(input(' enter the first number '))
 Y = int(input(' enter the second number '))
 sign = input(' enter the sign of the equation ')
 if sign == '+':
     Z = X + Y
 elif sign == '-':
     Z = X - Y
 elif sign == '*':
     Z = X * Y
 elif sign == '/':
     if Y == 0:
         print('net resh')
         break
     Z = X / Y
 if sign != '0':
     print(Z)

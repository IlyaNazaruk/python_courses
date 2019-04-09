# Описать функцию fact2( n ) вещественного типа, вычисляющую двойной факториал :n!! = 1·3·5·...·n,
# если n — нечетное; n!! = 2·4·6·...·n,
# если n — четное (n > 0 — параметр целого типа.
# С помощью этой функции найти двойные факториалы пяти данных целых чисел
def factorial():
    counter = 0
    while counter != 5:
        counter += 1
        n = int(input('enter the number '))
        result = 1
        if n % 2 == 0:
            for i in range(1, n+1):
                if i % 2 == 0:
                    result *= i
                if i == n:
                    print(result,'-result of factorial')
            continue
        else:
            for i in range(1, n+1):
                if i % 2 != 0:
                    result *= i
                if i == n:
                    print(result, '-result of factorial')
            continue

    return result
factorial()

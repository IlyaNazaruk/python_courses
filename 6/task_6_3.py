# Два натуральных числа называют дружественными, если каждое из них
# равно сумме всех делителей другого, кроме самого этого числа. Найти все
# пары дружественных чисел, лежащих в диапазоне от 200 до 300. [02-3.2-HL02]
start = 200
end = 300
result = []
skip = []
for number in range(start,end):
    if number in skip:
        continue
    finish = int(number / 2)
    second_number = 0
    for counter in range(1, finish + 1):
        if number % counter == 0:
            second_number += counter
    sum = 0
    if second_number >= start and second_number <= end:
        finish = int(second_number / 2)
        for counter in range(1, finish + 1):
            if second_number % counter == 0:
                sum += counter
        if sum == number:
            result.append([number, second_number])
            skip.append(second_number)
print(result)

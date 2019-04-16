# Имеются два текстовых файла с одинаковым числом строк.
# Выяснить, совпадают ли их строки.
# Если нет, то получить номер первой строки, в которой эти файлы отличаются друг от друга.


def compare_lines(lines_1, lines_2):
    for number, line in enumerate(lines_1):
        if line != lines_2[number]:
            return number
    return -1


first_file = open('task_10_4_1.txt')
second_file = open('task_10_4_2.txt')
lines_1 = first_file.readlines()
lines_2 = second_file.readlines()
first_file.close()
second_file.close()

result = compare_lines(lines_1, lines_2)
if result == -1:
    print('files are the same')
else:
    print('the bad line is', result)

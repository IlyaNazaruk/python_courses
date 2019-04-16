# Имеется текстовый файл. Все четные строки этого файла записать во второй файл,
# а нечетные — в третий файл. Порядок следования строк сохраняется.[03-15.29]

even_file = open('task_10_3_1.txt')
with open('task_10_3_2.txt', 'w') as f_o1:
    with open('task_10_3_3.txt', 'w') as f_o2:
        lines = even_file.readlines()
        f_o1.writelines(lines[::2])
        f_o2.writelines(lines[1::2])
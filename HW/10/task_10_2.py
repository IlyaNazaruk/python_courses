# Имеется текстовый файл. Переписать в другой файл
# все его строки с заменой в них символа 0 на символ 1 и наоборот. [03-15.28]

my_file = open('task_10_2_1.txt')
new_file = open('task_10_2_2.txt', 'a')
new_file.write('\n')
replaces = {
    '0': '1',
    '1': '0'
}
for line_1 in my_file:
    print(line_1)
    new_line = ''
    for character in line_1:
        if character in replaces:
            new_line += replaces[character]
        else:
            new_line += character
    new_file.write(new_line)
my_file.close()
new_file.close()
new_file = open('task_10_2_2.txt')
print('#####################')
for line in new_file:
    print(line)

#
# my_file = open('task_10_1.txt', 'a')
# for sent in range(3):
#     sentence = input('write some sentence ' )
#     my_file.write(sentence + '\n')
# my_file.close()


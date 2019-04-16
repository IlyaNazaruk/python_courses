# В конец существующего текстового файла записать три новые строки текста.
# Записываемые строки вводятся с клавиатуры.[03-15.6]

my_file = open('task_10_1.txt', 'a')
for sent in range(3):
    sentence = input('write some sentence ' )
    my_file.write(sentence + '\n')
my_file.close()
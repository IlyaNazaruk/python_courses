# В заданной строке расположить в обратном порядке все слова.\
# Разделителями слов считаются пробелы.[02 - 7.2 - HL08]
words = 'lasd qwer qwe prtoq adlfk '
len_words = len(words)
list_of_words = []
counter = 0
for i in range(len_words):
    if words[i] == ' ':
        list_of_words.append(words[counter:i])
        counter = i
last_word = []
i = -1
# while words[i] != ' ':
#     last_word.append(words[i])
#     i -= 1

print(list_of_words[::-1])
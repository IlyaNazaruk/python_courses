# Дан список строк. Отформатировать все строки в формате ‘{i} - {string}’,
# где i это порядковый номер строки в списке. Использовать генератор списков.
sentences = ['put some peace of pie', 'cat is very beautifukl', 'I have soam']
length = len(sentences)
new_dict = ((lambda sentences:['{}-{}'.format(i, sentences[i])
                            for i in range(length)])(sentences))
print(new_dict)




# print((lambda list_a: ['hello,{}'.format(name) for name in list_a])(list_a))

# Создать lambda функцию, которая принимает на вход неопределенное количество
# именных аргументов и выводит словарь с ключами удвоенной длины. {‘abc’: 5} -> {‘abcabc’: 5}

diction = {'aa' : 1,'casd' : 123}
print((lambda diction: dict(('{}'.format(key*2),value) for key, value in diction.items()))(diction))

# Даны три слова.Выяснить, является ли хоть одно из них палиндромом("перевертышем"), \
# т.е.таким, которое читается одинаково слева направо и справа налево.
# (Определить функцию, позволяющую распознавать слова палиндромы.)[03 - 10.32]
def palindrom(*words):
    for word in words:
        length = len(word) // 2
        for i in range(length):
            if word[i] == word[-1 - i]:
                if i + 1 == length:
                    print(word)
words = ['ooppoo', 'qewreq', 'iotoi']
palindrom(*words)
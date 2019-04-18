# Создать пять классов описывающие реальные объекты.
# Каждый класс должен содержать минимум три приватных атрибута,
# конструктор, геттеры и сеттеры для каждого атрибута, два метода.


class Thing:
    def __init__(self, figure, color, size):
        self.__figure = figure
        self.__color = color
        self.__size = size

    @property
    def open_window(self):
        print('Open pr')

    def close_window(self):
        print('Close pr')


    @property
    def figure(self):
        return self.__figure

    @figure.setter
    def figure(self, figure):
        self.__figure = figure

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color


    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        self.__size = size


thing = Thing('circle', 'white', '50')
thing.open_window
thing.close_window()
print(thing.figure)
thing.figure = 'square'
print(thing.figure)
print(thing.color)
thing.color = 'black'
print(thing.color)
print(thing.size)
thing.size = '80'
print(thing.size)
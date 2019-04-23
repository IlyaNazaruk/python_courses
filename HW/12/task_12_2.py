# Создать класс MyTime. Атрибуты: hours, minutes, seconds.
# Методы: переопределить магические методы сравнения, сложения, вычитания, умножения на число, вывод на экран.
# Перегрузить конструктор на обработку входных параметров вида:
# одна строка, три числа, другой объект класса MyTime, и отсутствие входных параметров.
# Примечание: http://sheregeda.github.io/blog/2015/01/18/maghichieskiie-mietody-python/
class MyTime:
    def __init__(self, hours=0, minutes=0, seconds=0):
        if isinstance(hours, str):
            hours, minutes, seconds = [int(i) for i in hours.split()]
        self.minutes = minutes
        self.minutes += seconds // 60
        self.seconds = seconds % 60
        self.hours = hours
        self.hours += self.minutes // 60
        self.minutes = self.minutes % 60
        if self.seconds < 0:
            self.seconds += 60
            self.minutes -= 1
        if self.minutes < 0:
            self.minutes += 60
            self.hours -= 1

    def __eq__(self, time):
        if self.hours == time.hours:
            if self.minutes == time.minutes:
                if self.seconds == time.seconds:
                    return self == time

    def __gt__(self, time):
        if self.hours >= time.hours:
            if self.minutes >= time.minutes:
                if self.seconds > time.seconds:
                    return self > time

    def __lt__(self, time):
        if self.hours <= time.hours:
            if self.minutes <= time.minutes:
                if self.seconds < time.seconds:
                    return self < time

    def __add__(self, time):
        sum_hours = self.hours + time.hours
        sum_minutes = self.minutes + time.minutes
        sum_seconds = self.seconds + time.seconds
        return MyTime(sum_hours, sum_minutes, sum_seconds)

    def __mul__(self, number):
        self.hours *= number
        self.minutes *= number
        self.seconds *= number
        return MyTime(self.hours, self.minutes, self.seconds)

    def __sub__(self, time):
        dif_hours = self.hours - time.hours
        dif_minutes = self.minutes - time.minutes
        dif_seconds = self.seconds - time.seconds
        return MyTime(dif_hours, dif_minutes, dif_seconds)

    def __str__(self):
        return '{} hours {} minutes {} seconds'.format(self.hours, self.minutes, self.seconds)


time_1 = MyTime(1, 61, 50)
time_2 = MyTime(2, 78, 40)
time_zero = MyTime('1 1 1')
print(time_zero)
print(time_1 + time_2)
print(time_2 - time_1)
print(time_1 * 2)
if time_1 < time_2:
    print('>>>>>>>>>>>')
else:
    print('<<<<<<<<<<<<<<')

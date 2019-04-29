from random import randint


class Matrix:
    def __init__(self, m=5, n=5, data=None):
        if not data:
            data = [[randint(0, 10) for _ in range(n)] for _ in range(m)]
            self.n = n
            self.m = m
        else:
            self.n = len(data[0])
            self.m = len(data)
        self.data = data

    def __str__(self):
        result = ''
        for row in self:
            for elem in row:
                result += str(elem) + ' '
            result += '\n'
        return result

    def __getitem__(self, i):
        return self.data[i]

from exceptions import MathException, NumberException


class Math:
    def __init__(self):
        pass

    def check_args(self, args):
        if len(args) != 3:
            raise MathException('nepravilnoe kolichestvo arguemntov')
        if args[1] not in ['+', '/', '-', '*']:
            raise MathException('nepravilni znak')
        if not args[0].isnumeric():
            raise NumberException('nepravilno first chislo')
        if not args[2].isnumeric():
            raise NumberException('nepravilno second chislo')

    def add(self, arg1, arg2):
       sum = arg1 + arg2
       return sum

    def mul(self, arg1, arg2):
       multiplic = arg1 * arg2
       return multiplic

    def sub(self, arg1, arg2):
       subtraction = arg1 * arg2
       return subtraction

    def div(self, arg1, arg2):
       division = arg1 / arg2
       return division

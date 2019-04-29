from exceptions import MathException

def check_args(args):
    if len(args) != 3:
        raise MathException('nepravilnoe kolichestvo arguemntov')
    if args[1] not in ['+', '/', '-', '*']:
        raise MathException('nepravilni znak')
    if not args[0].isnumeric():
        raise MathException('nepravilno first chislo')
    if not args[2].isnumeric():
        raise MathException('nepravilno second chislo')

def add(arg1, arg2):
   sum = arg1 + arg2
   return sum

def mul(arg1, arg2):
   multiplic = arg1 * arg2
   return multiplic

def sub(arg1, arg2):
   subtraction = arg1 * arg2
   return subtraction

def div(arg1, arg2):
   division = arg1 / arg2
   return division

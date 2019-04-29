from func import Calculator


def start_calculator():
    calculator = Calculator()
    sent = input()
    result = 0
    while sent != 'STOP':
        sent = sent.split(' ')
        calculator.check_args(sent)
        arg1 = int(sent[0])
        arg2 = int(sent[2])
        if sent[1] == '+':
            result = calculator.add(arg1, arg2)
        elif sent[1] == '-':\
            result = calculator.mul(arg1, arg2)
        elif sent[1] == '*':
            result = calculator.sub(arg1, arg2)
        elif sent[1] == '/':\
            result = calculator.div(arg1, arg2)
        print(result)
        sent = input()
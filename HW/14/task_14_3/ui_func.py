import func


def start_calculator():
    sent = input()
    result = 0
    while sent != 'STOP':
        sent = sent.split(' ')
        func.check_args(sent)
        arg1 = int(sent[0])
        arg2 = int(sent[2])
        if sent[1] == '+':
            result = func.add(arg1, arg2)
        elif sent[1] == '-':\
            result = func.mul(arg1, arg2)
        elif sent[1] == '*':
            result = func.sub(arg1, arg2)
        elif sent[1] == '/':\
            result = func.div(arg1, arg2)
        print(result)
        sent = input()
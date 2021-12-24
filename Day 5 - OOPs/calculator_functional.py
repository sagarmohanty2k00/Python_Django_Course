def add(a, b):
    return a+b

def sub(a, b):
    return a-b

def mul(a, b):
    return a*b

def div(a, b):
    return a/b

def calculator():
    while True:
        a, op, b = input().split()

        if op == '+':
            print(add(int(a), int(b)))

        if op == '-':
            print(sub(int(a), int(b)))

        if op == '/':
            print(div(int(a), int(b)))

        if op == '*' or op == 'x':
            print(mul(int(a), int(b)))

calculator()
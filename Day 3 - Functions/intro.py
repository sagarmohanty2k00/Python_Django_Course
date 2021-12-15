def name(p1, p2):
    # logic
    return 0

def add(a ,b):
    return a+b

# formal argument examople
def increament(a):
    a += 10

a = 4
b = 5
# print(add(a, b))
# increament(a)
# print(add(a, b))

# return examples
def returnVal(a):
    return a+10

def returnMulty(a, b):
    return a+1, b+1

# a = returnVal(a)
# print(a)

# a, b = returnMulty(a, b)
# print(a)
# print(b)


# Arguments
def args(a, b):
    print(a)
    print(b)

def default(a, b, c=5):
    return a+b+c

# args(4, 5)
# args(5, 4)
# args(b=4, a=5)
print(default(1,2))
print(default(1,2,3))
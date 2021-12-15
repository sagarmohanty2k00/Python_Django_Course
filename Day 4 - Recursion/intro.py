# function to function
def first():
    print("Hello")

def second():
    first()
    print("World")

# second()

# recursion - template
def rec():
    rec()

# sum upto n
def sum(n):
    sum = 0
    for i in range(n+1):
        sum += i

    return sum

def sumRec(n):
    if n <= 0:
        return 0

    return sumRec(n-1) + n

# print(sum(10))
# print(sumRec(10))

# sum of 'n' elements = sum  of 'n-1' + n
# f(10) = f(9) + 10
# f(9) = f(8) + 9
# f(8) = f(7) + 8
# ...
# f(1) = f(0) + 1
# f(0) = 0

# Recursion works like magic


# fibonacci = 1 1 2 3 5 8 13 21 33 ...
def fib(n):
    # base condition
    if n == 0 or n == 1:
        return 1

    return fib(n-1) + fib(n-2)

print(fib(10))
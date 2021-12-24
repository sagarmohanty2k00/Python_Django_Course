l = [1 ,2 ,3]

try:
    print(l[2])
except:
    print("Out  of bound")


a = int(input())
b = int(input())

try:
    c = ((a+b)/(a-b))
except NameError:
    print("Name error")
except ZeroDivisionError:
    print("divided by 0")
else:
    print(c)
finally:
    print("Finally")
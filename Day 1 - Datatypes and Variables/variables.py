a = int()           # Declaration
print(str(a) + str(type(a)))

a = 10              # Initialization
a -= 10
a *= 12
a = a / 2
print(str(a) + str(type(a)))

a = "sagar"
print(str(a) + str(type(a)))

a += "mohanty"
a = a + "mohanty"
print(str(a) + str(type(a)))

## Naming rules
# not a number
# not a special char
# not a keywords


### User Input
print("Enter the value for val1 : ", end='')
val1 = input()      # User Input
print(val1)

val2 = int(input("Enter the value for val2 : "))  # Typecasting
print(val2*2)
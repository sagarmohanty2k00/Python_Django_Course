# Conditions
# <, >, <=, >=, ==, != 
# and, not, or, in

# Results
# True, False, 1, 0

a = 10
print(a < 10)
print(a > 10)
print(a <= 10)
print(a >= 10)
print(a == 10)
print(a != 10)

# IF statements
if a == 10:
    print("a is 10")
    print("error message")

if a != 10:
    print("a is not 10")

# if (a == 10) {
#     print()
# }

# If Else
if a != 10:
    print("a is not 10")
else :
    print("a is 10")


# Elif
going_to_school = False
class_topper = True

if going_to_school and class_topper:
    print("Will get a motor-cycle.")
elif going_to_school or class_topper:
    print("Will get a cycle.")
else :
    print("Will not get anything.")


if not class_topper:
    print("Not the topper")
else :
    print("He is the topper")

# Use of in
basket = ["Apple", "Banana", "Melon", "Berry"]
fruit = "Berry"
if fruit in basket:
    print("Fruit is in the basket")
else :
    print("Add the fruit to the basket")

if "rr" in fruit:
    print("It's a berry")
else:
    print("It's not a berry")

import random

list1 = [1, 2, 3, 4, 5, 6]
print(random.choice(list1))
print(random.randint(0, 7))


r1 = random.randint(5, 15)
print("Random number between 5 and 15 is % s" % (r1))

print(random.random())
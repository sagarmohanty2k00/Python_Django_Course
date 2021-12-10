# 3 types of strings
str1 = 'Rakesh Kumar'
str2 = "Rakesh Kumar"
str3 ='''
Rakesh
            Kumar
'''
str4 = """Rakesh Kumar"""  # Doc string

print("Rakesh's laptop")
print('"Rakesh" is a good boy')

print(str1)
print(str2)
print(str3)

# functions
print(str1.lower())
print(str2.upper())

# indexing
print(str1[0])
print(str1[-1])
print(str1[-4])

# Slicing
# print(str1[from:to+1])
print(str1[::-1])  # reverse a string
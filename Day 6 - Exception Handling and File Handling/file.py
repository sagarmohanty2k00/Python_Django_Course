# fileVariablename = open(fileName, mode)
# r(read), w(write), a(append)

# Operation 1 : write
# open a file
# write() function
# close() the file

myFile = open("pyTuts.py", 'w')
myFile.write('''print("Hello World")''')
myFile.close()

# Operation 2 : append

myFile = open("pyTuts.py", 'a')
myFile.write("\n# taking input")
myFile.write("\na = int(input())")
myFile.close()


# Operation 3 : Read
myFile = open("pyTuts.py", 'r')
print(myFile.readline())

for line in myFile.readlines():
    print(line)

myFile.close()


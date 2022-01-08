# 1 2 3 4 5
# LIFO

class Stack:
    def __init__(self, size):
        self.size = size
        self.top = -1
        self.items = [0]*size

    def push(self, item):
        if self.top == self.size-1:
            print("stack overflow")
        else:
            self.top += 1
            self.items[self.top] = item

    def pop(self):
        if self.top == -1:
            print("stack underflow")
        else:
            self.top -= 1

    def top(self):
        if self.top != -1:
            return self.items[self.top]
        else:
            return -1

    def traverse(self):
        pos = self.top
        while pos > 0:
            print (self.items[pos], end=' ')
            pos -= 1

    def empty(self):
        return self.top == -1

stk = Stack()

while 1:
    print("1. push")
    print("2. pop")
    print("3. traverse")
    print("4. top")
    print("5. empty")
    print("6. break")

    choice = int(input())

    if choice == 1:
        print ("Enter data : ", end='')
        data = int(input())

        # 


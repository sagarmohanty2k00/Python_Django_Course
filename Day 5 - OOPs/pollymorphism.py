class A:
    def div(self, a, b):
        return a//b

class B(A):
    def div(self, a, b):
        return a/b

b = A()
print(b.div(4, 2))
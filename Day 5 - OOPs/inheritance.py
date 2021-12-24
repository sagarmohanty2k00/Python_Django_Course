class Parent:
    age = None
    name = None

    def __init__(self, age, name) -> None:
        self.name = name
        self.age = age

    def changeAge(self, newAge):
        self.age = newAge

# single inheritance
class Child(Parent):
    def tellAge(self):
        print(self.age)

# Multi level Inheritance
class GrandChild(Child):
    def tellName(self):
        print(self.name)


class Father:
    name = None

    def tellName(self):
        print(self.name)

class Mother:
    age = None

    def tellAge(self):
        print(self.age)

# Multiple Inheritance
class Offspring(Father, Mother):
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

parent = Parent(age=34, name="Rakesh")
child = Child(age=34, name="Rakesh")
child.changeAge(22)
child.tellAge()

gchild = GrandChild(age=13, name="Suresh")
gchild.tellName()


off = Offspring(name="offspring", age=14)
off.tellName()
off.tellAge()
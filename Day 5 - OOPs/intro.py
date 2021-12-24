# Programing paradigms => Structural, Functional, Object Oriented


## Class
class Car:
    wheels = 4
    engine = None
    color = None

    def __init__(self, wheels, engine, color):  # constructor
        self.wheels = wheels
        self.engine = engine
        self.color = color


    def start(self, owner):
        print(owner + " started the car")

    def stop(self):
        print("car stopped")

## Objects
car1 = Car(4, 'v8', 'white')

# class variables
# instance variable
car1.owner = 'sagar mohanty'

car1.start("rakesh")
car1.stop()

# Pollymorohism

# Encapsulation

# Inheritance

# Abstraction

a = 10

def greeet():
    message = "Good morning"

    if message == "Good morning":
        print(message)
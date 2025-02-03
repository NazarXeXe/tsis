
class Human:
    def __init__(self, name):
        self.name = name
        self.drink = lambda: print("I'm drinking...")
    def eat(self):
        print( f"{self.name}: I'm eating" )

class Student(Human):
    def study(self):
        print(f"{self.name}: I'm studying")

def myFunction(human: Human):
    print(f"{human.name}: hi")

def optional(yo=50):
    print(f"{yo}")

def varArg(*args):
    for i in args:
        print(i)

def kvArgs(**args):
    for i in args:
        print(i, args[i])

if (__name__ == "__main__"):    
    human = Human('Bob')
    student = Student('Alex')
    human.eat()
    student.eat()
    human.drink()
    student.drink()

    group = [
        Student('Alice'),
        Human('John'),
        Human('James'),
        Student('Jack')
    ]

    myFunction(human)
    optional()
    optional(70)

    varArg(1,2,2)
    kvArgs(hello=1, bye=2)

    for human in group:
        if type(human) is Student:
            human.study()
        else:
            human.eat()

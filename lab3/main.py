class Human:
    def __init__(self, name):
        self.name = name
        self.drink = lambda: print("I'm drinking...")
    def eat(self):
        print( f"{self.name}: I'm eating" )

class Student(Human):    
    def study(self):
        print(f"{self.name}: I'm studying")

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
        Student('Jacl')
    ]

    for human in group:
        if type(human) is Student:
            human.study()
        else:
            human.eat()

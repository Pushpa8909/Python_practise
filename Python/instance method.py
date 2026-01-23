#instance method
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print('Hi', self.name)
        print('Your Marks are:', self.marks)

    def grade(self):
        if self.marks >= 60:
            print('You got first grade')
        elif self.marks >= 50:
            print('You got second grade')
        elif self.marks >= 35:
            print('You got third grade')
        else:
            print('You are failed')
n = int(input('Enter number of students: '))

for i in range(n):
    name = input('Enter your name: ')
    marks = int(input('Enter the marks: ')) 
    s = Student(name, marks)
    s.display()
    s.grade()
    print('End\n')

#Class method
class Animal:
    legs = 4
    @classmethod
    def walk(cls, name):
        print('{} walks with {} legs.'.format(name, cls.legs))
Animal.walk('Dog')
Animal.walk('Cat')

#static method
class Aditya:
    @staticmethod
    def add(x,y):
        print('The sum value is ',(x+y))
    def sub(x,y):
        print('The difference value is ',(x-y))
    def avg(x,y):
        print('The average value is ',(x+y)/2)
Aditya.add(200,100)
Aditya.sub(200,100)
Aditya.avg(200,100)


#Destructor
class Student:
    def __del__(self):
        print("\nDestructor called, object deleted")
s = Student()
del s

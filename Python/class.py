class Car:
    def __init__(self, make, model, year, color):  
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.speed = 0

car1 = Car("Toyota", "Camry", 2022, "Red")
car2 = Car("Ford", "Mustang", 2023, "Black")

print(car1.make)     
print(car2.speed)
print(car1.year)

class Student:
    def __init__(self, name, roll_no, year, branch, cgpa):
        self.name = name
        self.roll_no = roll_no
        self.year = year
        self.branch = branch
        self.cgpa = cgpa
        self.attendance = 80  

student1 = Student("Pravallika", "24B11CS!25", 2, "CSE", 9.2)
student2 = Student("Sruthi", "24B11CS113", 2, "CSE", 9.1)

print(student1.name)
print(student1.roll_no)
print(student1.year)
print(student1.branch)
print(student2.cgpa)  

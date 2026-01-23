class Student:
    def __init__(self, name, roll_no): 
        self.name = name
        self.roll_no = roll_no
        print("Inside Constructor:")
        print("Name:", self.name)
        print("Roll Number:", self.roll_no)

    def update_marks(self, marks):
        self.marks = marks
        print("\nInside Instance Method:")
        print(f"{self.name}'s Marks:", self.marks)

s1 = Student("Anil", 101)
s1.update_marks(95)



class student:
    def __init__(self, name, roll_no):  
        self.name = name               
        self.roll_no = roll_no
        print("Inside Constructor:")
        print("Name:", self.name)
        print("Roll No:", self.roll_no)

    def update_marks(self, marks):     
        self.marks = marks
        print("\n\nInside Instance Method:")
        print(f"{self.name}'s Marks Updated to:", self.marks)

s1 = student("Kalyan", 101)


#Static variable
class Test:
    x = 10  
    def __init__(self):
        self.y = 20     

t1 = Test()
t2 = Test()
print('t1:', t1.x, t1.y)
print('t2:', t2.x, t2.y)
Test.x = 888
t1.y = 999      
print('t1:', t1.x, t1.y)
print('t2:', t2.x, t2.y)




#Local variable
class Test:
    def m1(self):
        a=1000
        print('\n')
        print(a)
    def m2(self):
        b=2000
        print(b)
t=Test()
t.m1()
t.m2()


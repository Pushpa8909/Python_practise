my_set={1,2,3,4,5}
my_set.add(6)
my_set.remove(2)
print(3 in my_set)
print("my_set",my_set)

student={"name":"jhon","age":20,"grade":"A"}
print("name:",student["name"])
student["city"]="hyderabad"
student["age"]=21
del student["grade"]
print("student details",student)

start=int(input("enter the start of the intervel"))
end=int(input("enter the end of the intervel"))
print("prime number between",start,"and",end,"are")
for num in range(start,end+1):       
    if num>1:
      for i in range(2,num):
         if num%i==0:
            break;
         else:
           print(num);
a = 10  
b = 5  

print("Addition:", a + b)           
print("Subtraction:", a - b)      
print("Multiplication:", a * b)  
print("Division:", a / b)         
print("Modulus:", a % b)          
print("Exponentiation:", a ** b)   
print("Floor Division:", a // b)

member1 = ("Alice", 22, "123 Maple St", "ABC University")  
member2 = ("Bob", 23, "456 Oak Ave", "XYZ College")  
concatenated_tuple = member1 + member2   
print("Concatenated Tuple:", concatenated_tuple)

start = int(input("Enter the start of the interval: "))  
end = int(input("Enter the end of the interval: "))  

print("Prime numbers between", start, "and", end, "are:")  

for num in range(start, end + 1):  
    if num > 1:  
        for i in range(2, num):  
            if num % i == 0:  
                break  
        else:  
            print(num)
            
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("number is even")
else:
    print("number is odd")

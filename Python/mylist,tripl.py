mylist=[12,3,4,21,65];
print(mylist[2:4]);
print(mylist[2:]);
print(mylist[-4:-1]);
print(mylist[:-1]);
print(mylist[-4:]);
mylist[3]="apple";
print(mylist);
mylist[1:3]=["hello","Hai"];
print(mylist);
mylist.insert(2,"CSE");
print(mylist);
for n in mylist:
    print(n);
print(12 in mylist)

mytriple=(12,'apple',True,19.5);
print(mytriple);
mylist=list(mytriple)


def fibonocci(n):
    if(n<=0):
        print("Invalid input")
    elif(n==1):
        return 0;
    elif(n==2):
        return 1;
    else:
        return fibonocci(n-1)+fibonocci(n-2);
print
print(fibonocci(5))

#1
'''i=0
while(i<11):
    n=input("enter a no")
    print(n)
    i=i+1
print("\n")
#2
while True:
    print("INFINITE")'''

#3
numbers=[]
for i in range(0,5):
    num=int(input("enter a no"))
    numbers.append(num)
print("the list is",numbers)
squares=[]
for num in numbers:
    sq=num*num
    squares.append(sq)
print("the new list is",squares)
print("\n")

#4
l=[6,'isha',4.45,12,'shivi',2.3]
for i in l:
    print("the type is",i,"is",str(type(i)))
print("\n")

#5
even=[]
odd=[]
for i in range(1,101):
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("list for even no is",even)
print("list for odd no is",odd)
print("\n")

#6
i=1
while i<=4:
    print("*"*i)
    i=i+1
print("\n")

#7
val={'rohru':'ishu','jammu':'shivi','kangra':'prachi'}
for key in val.keys():
    print(key,val[key])
print("\n")

#8
l=['orange','mango','apple','grapes']
name=input("enter the name of fruits")
for fruit in l:
    if fruit==name:
        print("available")
        l.remove(fruit)
        print("list",l)

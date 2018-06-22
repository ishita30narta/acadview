#1
print("Python store time in tuples and these tuples are made up of nine numbers and these nine numbers are 0 to 9 which are index")

#2
import time
print (time.strftime("%H:%M:%S"))

#3
import datetime,time
print(time.strftime("%b"))

#4
import datetime,time
print(time.strftime("%a"))

#5
import datetime,time
print(time.asctime(time.localtime()))
print(time.strftime("%d"))

#6
import datetime,time
print(time.asctime(time.localtime()))

#7
n=int(input("Enter a no:"))
import math
print(math.factorial(n))

#8
x=int(input("Enter a no:"))
y=int(input("Enter a no:"))
import math
print(math.gcd(x,y))

#9
import os
print(os.name)
print(os.environ)
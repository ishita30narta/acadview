# paymen gateway............

#exceptional handling: improve the readibility
'''try:
 a=10
 b=3/a
except ZeroDivisionError:
  print("No is divisible by zero")

else:   #if zero divisible erroe nt find then else
    print(a)

finally:
    print("I will execute")

try:
 import ishita
 a=[1,2,3]
 print(a[3])
except ZeroDivisionError:          #IndexError:
  print("No is divisible by zero")
except IndexError:
  print("index doesn't exist")
except ImportError:
  print("doesn't exist")

class AgeError(Exception):  #exception class extend
    pass
try:
    a=int(input("enter age"))
    if(a<18):
        raise AgeError
except ValueError:
    print("please enter int")
except AgeError:
    print("under age")
else:
    print("you are eligible")

try:
    raise NameError("Hi there")
except NameError:
    print("An exception")'''

def AbyB(a ,b):
    try:
        c =





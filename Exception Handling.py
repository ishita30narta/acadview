#1
print("ZeroDivisionError occur in this")
try:
    a = 3
    if a < 4:
        a = a / (a - 3)
        print(a)
except ZeroDivisionError:
    print("No is Divisible by Zero")
print("\n")

#2
print("IndexError occur in this")
try:
    l=[1,2,3]
    print(l[3])
except IndexError:
    print("Index doen't found")
print("\n")

#3
print("An Exception will be the output")
print("\n")

#4
def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print("a/b result in 0")
	else:
		print(c)

# Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)
print("\n")

#5
#5(1). Import Error
try:
    import ishita
except ImportError:
    print("Doesn't exist")

#5(2). Value Error
try:
   a=int(input("enter a value"))
except ValueError:
   print("Enter integer value")

#5(3). Index Error
try:
    a=[1,2,3,4]
    print(a[4])
except IndexError:
    print("Index doesn't found")
print("\n")

#6.
class AgeTooSmallError(Exception):
    pass
try:
    a=int(input("Enter a age"))
    if a<18:
        raise AgeTooSmallError
except AgeTooSmallError:
    while a<=18:
        a=int(input("enter age again"))


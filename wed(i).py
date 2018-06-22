#1
rad=float(input("Enter a no"))
def area(rad):
    area=3.14*rad*rad
    return area
ar=area(rad)
print(ar)

#2
n=6
def perfect(n):
    sum=0
    for i in range (1,n):
        if(n%i==0):
            sum=sum+i
    if(sum==n):
         return True
    else:
         return False

for i in range(1,1001):
 if(perfect(i)==True):
     print(i)

#3
def mul(i):
    if i<=10:
      a=12*i
      print(a)
      i=i+1
      mul(i)

mul(1)

#4
a=int(input("Enter a no"))
b=int(input("Enter a no"))
def power(x,y):
    if(y==1):
        return x
    else:
        return x*power(x,y-1)

print(power(a,b))

#5
n=int(input("Enter a no"))
d={}
def fact(i):
    if(i==0):
         return 1
    else:
         return (i*fact(i-1))


for i in range (1,n+1):
    d[i]=fact(i)
print(d)


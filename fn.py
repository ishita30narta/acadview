'''def fn():
    print("Hello")

fn()

def add(a,b):
    c=a+b
    print(c)

    a=2
    b=3

add(a,b)
def add(a,b):
    d=a*a
    c=b*b*b
    print(d,c)

add(2,3)
def add(a,b):
    d=a*a
    c=b*b*b
    return d,c

a,b=add(2,3)
print(a,b)

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


print(perfect(n))
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
     print(i)'''




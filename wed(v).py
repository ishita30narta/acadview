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




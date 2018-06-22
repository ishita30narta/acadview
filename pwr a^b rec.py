a=int(input("Enter a no"))
b=int(input("Enter a no"))
def power(x,y):
    if(y==1):
        return x
    else:
        return x*power(x,y-1)

print(power(a,b))
#1
tup1 =('python','c','java')
tup2 =(1,2,3,4)
tup3 =(1.3,3.6,7.8)
print(len(tup1+tup2+tup3))
print("\n")

#2
tup =(2,4,5,7)
print(min(tup))
print(max(tup))
print("\n")

#3
x=1
y=(1,2,3,4)
for i in y:
    x=x*i
print(x)
print("\n")


#4
n =set([1,2,3,8])
m =set([3,4,5])
o =n & m      #(ii) comparison of two sets
p=n-o #(i) difference b/w tw sets
q=o-p
print(p)
print(q)
print(o)   #(iii) interstion of two sets
print("\n")

#5
a=input("enter a student name :")
b=input("enter a marks :")
d={}
def b(i):
    for i in b:
        k=b[i]
        return k

for j in a:
    d[j]=b(i)
pri(d)

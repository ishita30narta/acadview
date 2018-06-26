#1
n=input("Enter a list:")
l=[]
l.append(n)
print(l)
print("\n")

#2
a=["google","apple","facebook","microsoft","tesla"]
a.append(l)
print(a)
print("\n")

#3
b=[1,2,3,4,4,5,4]
b.count(4)
print(b.count(4))
print("\n")

#4
c=[2,4,1,5]
c.sort()
print(c)
print("\n")

#5
arr1 = [1,3,4,5]
arr2 = [2,6,8]
arr3 =sorted(sorted(arr1) + sorted(arr2))
print(arr3)
print("\n")

#6
stack =["Ishita","Prachi","Shivangi","Akanksha"]
stack.append("Sayima")
stack.append("Rashika")
print(stack)
print(stack.pop())


queue =["Ishita","Prachi","Shivangi","Akanksha"]
print(queue)
queue.append("Aanchal")
print(queue)
queue.pop()
print(queue)


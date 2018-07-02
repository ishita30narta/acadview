#1
f=open("file.txt",encoding="utf8")
j=(f.readlines())
j.reverse()
n=int(input("enter a no. of line you want to"))
for i in range(0,n):
    print(j[i])
f.close()

#2
n="to"
f=open("file.txt",encoding="utf8")
k=f.read()
m=k.split()
print(k.count(n))

#3
f=open("file.txt",encoding="utf8")
f=f.readlines()
f1=open("file2.txt","w",encoding='utf8')
f1.writelines(f)


#4
fh = open('file.txt','r',encoding='utf8')
fh2 = open('file2.txt','r',encoding='utf8')
o = open('file3.txt','w',encoding='utf8')

for line in fh.readlines():
    o.write(line.strip() + fh2.readline().strip() + "\n")

fh.close()
fh2.close()
o.close()

#5
import random
with open("Random.txt","w")as f:
    for i in range(int(input('enter the random no. ?'))):
        line=str(random.randint(1,100))
        f.writelines(line + '\n')
        print(line)

with open("Random.txt")as f1,open("Random1.txt","w")as f2:
    lines = f1.read().splitlines()
    lines.sort()

for l in lines:
    f2.write(str(l) + '\n')
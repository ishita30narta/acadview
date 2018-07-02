#1
f=open("filehandlng.txt",encoding="utf8")
j=(f.readlines())
j.reverse()
n=int(input("enter a no. of line you want to"))
for i in range(0,n):
    print(j[i])
f.close()

#2
n="to"
f=open("filehandlng.txt",encoding="utf8")
k=f.read()
m=k.split()
print(k.count(n))

#3
f=open("filehandlng.txt",encoding="utf8")
f=f.readlines()
f1=open("filehandlng2.txt","w")
f1.writelines(f)


#4
fh = open('filehandlng.txt','rb')
fh2 = open('filehandlng2.txt','rb')
o = open('filehandlng3.txt','wb')

for line in fh.readlines():
    o.write(line.strip() + fh2.readline().strip())

fh.close()
fh2.close()
o.close()

#5
afile = open("filehandlng.txt", "w" )

for i in range(int(input('How many random numbers?: '))):
    line = str(random.randint(1, 100))
    afile.write(line)
    print(line)

afile.close()
# read,erit,append,read +
#f=open("text.txt","r")
#f=open("text.txt","a")
#f=open("text.txt","w")
#print(f)
#print(f.read())
#print(f.readline())
#print(f.readline())
#print(f.readlines())  #output in list

#list reverse,for loop
#f.write("hello")
#l=["a\n","b\n","c\n"]
#f.writelines(l)

#with keyword  is used to closed the running
with open("text.txt","r") as f:
   print(f.read(5))
   print(f.tell())
   f.seek(0,2)
   print(f.tell())

#f1.writef2,random.rand()
#1
'''tup1 =('python','c','java')
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
d = {}
count = 0
while count < 10:
      name = input("Enter your name: ")
      mark = input("Enter your mark out of 100: ")
      if name not in d:
          d[name] = mark
          count = count + 1

print(d)


#6
s="Misssssissippi"
count=0
character="i"

for i in s:
        if (i == character):
            count=count+1
print (count)
text="ishita"
def count_chars(text):
	result = 0
	for char in text:
		result += 1     # same as result = result + 1
	return result
print (count_chars(text))'''

s="Mississippi"
d={}
count=0
def abc(i):
    for i in s:
        if(i==abc[i]):
            count=count+1
    return count
for i in s:
    d[i]=abc(i)
print(d)
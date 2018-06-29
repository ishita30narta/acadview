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
print(o) #(iii) interstion of two sets
print(n>=m) #subset
print(n<=m) #superset
print("\n")



#5
import operator
d = {}
count = 0
while count < 3:
      name = input("Enter your name: ")
      mark = input("Enter your mark out of 100: ")
      if name not in d:
          d[name] = mark
          count = count + 1

print(d)
print("\n")
#6

sorted_d = sorted(d.items(), key=operator.itemgetter(0))
print('Sorted marks are : ',sorted_d)
print("\n")



#7
def count(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
print(count('Mississippi'))

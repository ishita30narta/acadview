#1
class Animal():
    def Animal_attribute(self):
        print("Zebra")
class Tiger(Animal):
        print("Lion")
a=Tiger()
a.Animal_attribute()
print("\n")

#2
class A:
    def f(self):
        return self.g()

    def g(self):
        return 'A'

class B(A):
    def g(self):
        return 'B'

a = A()
b = B()
print(a.f(), b.f())
print(a.g(), b.g())
#output will be A B,A B
print("\n")

#3
class Cop():
    def __init__(self,name,age,work_experience,designation):
      self.name=name
      self.age=age
      self.work_experience=work_experience
      self.designation=designation

    def add(self):
        print("Write DEtail about cop")

    def display(self):
        print(self.name)
        print(self.age)
        print(self.work_experience)
        print(self.designation)

    def Update(self,name,age,work_experience,designation):
       self.name1= name
       self.age1= age
       self.work_experience1=work_experience
       self.designation1= designation
       print(self.name1)
       print(self.age1)
       print(self.work_experience1)
       print(self.designation)

class Mission(Cop):

    def add_mission_details(self):
        print("Details about cop")

a=Mission("ABC",'20',"5 year of experience","Police")
a.add()
a.display()
a.Update("ABCDE",'25',"7 year of experience","Army")
print("\n")

#4
class Shape():
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth

class rectangle(Shape):
    def area(self):
       area=self.length*self.breadth
       print("area of rectangle :",area)

class square(rectangle):
    def area1(self):
        area1=self.length*self.length
        print("area of square :",area1)

a=square(3,4)
a.area()
a.area1()
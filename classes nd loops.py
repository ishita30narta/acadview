#1
class Circle():
    def __init__(self,radius):
        self.radius = radius
    def getArea(self):
        print(3.14*self.radius*self.radius)
    def getCircumference(self):
        print(self.radius*2*3.14)

c=Circle(radius=3)
c.getArea()
c.getCircumference()
print("\n")

#2
class Student():
    def __init__(self,name,rollno):
        self.name = name
        self.rollno = rollno
    def display(self):
        print(self.name)
        print(self.rollno)
    def setAge(self,age):
        self.age = age
        print(self.age)
a = Student("ishi",'99')
a.display()
a.setAge(20)
print("\n")

#3
class Temperature():
    def convertFahrenhiet(self,celsius):
        print((celsius*(4.0/3.0))+32.0)

    def convertCelsius(self,fahrenhiet):
        print((fahrenhiet-32.0)*(3.0/4.0))

t = Temperature()
t.convertCelsius(98.6)
t.convertFahrenhiet(37.5)
print("\n")

#4
class MovieDetails():
    def __init__(self,moviename,artistname,year,ratings):
        self.moviename=moviename
        self.artistname=artistname
        self.year=year
        self.ratings=ratings
    def display(self):
        print(self.moviename)
        print(self.artistname)
        print(self.year)
        print(self.ratings)
    def update(self,update):
        self.update=update
        print(self.update)
a=MovieDetails("Baagi 2","xyz",'2017','9/10')
a.display()
a.update('2018')
print("\n")

#5
class Expenditure():
    def __init__(self,expenditure,savings):
        self.expenditure=expenditure
        self.savings=savings
    def display(self):
        print(self.expenditure)
        print(self.savings)
    def total_salary(self,total_salary):
        self.total_salary = total_salary
        print(self.expenditure*total_salary/100)
        print(self.savings*total_salary/100)
    def display_salary(self,display_salary):
        self.display_salary=display_salary
        print(self.display_salary)

e=Expenditure(expenditure=5000,savings=10000)
e.display()
e.total_salary(30000)
e.display_salary(345214)

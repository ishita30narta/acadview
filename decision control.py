#1
year=int(input("Enter a year"))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("leap year")
       else:
           print("not a leap year")
   else:
       print("leap year")
else:
   print("not a leap year")

#2
l=int(input("enter length"))
b=int(input("enter breadth"))
if(l==b):
    print("dimensions are of square")
else:
    print("dimensions are of rectangle")

#3
a=int(input("enter age"))
b=int(input("enter age"))
c=int(input("enter age"))
if((a>b) and (a>c)):
    print("A is older")
else:
    print("A is younger")
if ((b>a) and (b>a)):
    print("B is older")
else:
    print("B is younger")
if ((c>a) and (c>a)):
    print("C is older")
else:
    print("C is younger")



#4
a=int(input("Enter the points scored :"))
if(a<=50):
    print ("Sorry!No prize this time.")

if(a>=51 and a<=150):
        print("Congratulations!You won a wooden dog")
elif(a>=151 and a<=180):
       print("Congratulations!You won a book")

if(a>=181 and a<=200):
    print("Congratulations!You won a chocolates")


#5
n=int(input("Enter the quantity of item:"))
c=n*100
if(c>1000):
    c= c*100-c/10
    print("Aftr discount cost is ")
    print(c)
else:
    print("No discount")
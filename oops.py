class Apolo():
    destination="Moon"
    def __init__(self):
        print("Ready to lauch")

    def flying(self):
        print("Spaceship is flying")

    def getdestination(self):
        print("The destination is"+ self.destination)

a=Apolo()
a.flying()
a.getdestination()
b=Apolo()
b.destination="Mars"
b.getdestination()
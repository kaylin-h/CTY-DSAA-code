class Animal:

    def __init__(self, newName):
        #self.name = "Franklin"
        self.name = newName

    def runs(self):
        print("My name is ", self.name, "and I run")

class Person:

    def __init__(self):
        self.name = ""
        self.lastname = ""
        self.ssn = 0
        self.height = 0

    def grows(self):
        self.height += 7

    def show_off(self):
        print("My name is ", self.fname, " ", self.lastname)

        print("My ssn is ". self.ssn)

        print("My height is ", self.height)
    


d = Animal("Dog")
print(d.name)
d.run

kay = Person()
kay.fname = "Kaylin"
kay.lastname = "h"
kay.ssn = 123455678
kay.height = 5
kay.show_off()

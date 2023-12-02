# Parent - Child
# Father -> son
# GF -> F -> S
# 1BHK -> 1 BHK -> 1BHK

# Single Inheritance

class Animal:

    def car(self):
        print("Lambo")
    def speak(self):
        pass
    def cry(self):
        print("cry")


class Dog(Animal):
    def speak(self):
        print("BOw Bow")
    def i_want_drive(self):
        Animal().car()



dog1 = Dog()
dog1.speak()
dog1.i_want_drive()
dog1.car()
dog1.cry()
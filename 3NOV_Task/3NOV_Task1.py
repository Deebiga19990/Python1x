# Create a Car class and Create 2 Objects of the class with attributes 5
# and 5 methods

class Car:
    name = None
    color = None
    model = None
    speed = None
    engine = None
    type = None
    def Transmission_Type(self):
        print("The transmission type is " +self.type)
    def Max_Speed(self):
        print("The Max Speed is " + self.speed)
    def Start_Engine(self):
        print("Start Engine")
    def Person_Driving(self):
        print("Im driving "+ self.name)
    def Stop_Engine(self):
            print("Stop Engine")

Toyota=Car()
Toyota.name="Toyota"
Toyota.color = "Grey"
Toyota.model = "Rev4"
Toyota.speed =  "120KMPH"
Toyota.engine = "E1"
Toyota.type = "Manual"
print("===================Object1===================")
print(f"Name:{Toyota.name},Color:{Toyota.color},model:{Toyota.model}"
      f",speed:{Toyota.speed},engine:{Toyota.engine}")
Toyota.Start_Engine()
Toyota.Transmission_Type()
Toyota.Person_Driving()
Toyota.Max_Speed()
Toyota.Stop_Engine()

Honda=Car()
Honda.name="Honda"
Honda.color = "Black"
Honda.model = "Autos"
Honda.speed =  "130KMPH"
Honda.engine = "E2"
Honda.type = "Automatic"
print("===================Object2===================")
print(f"Name:{Honda.name},Color:{Honda.color},model:{Honda.model}"
      f",speed:{Honda.speed},engine:{Honda.engine}")
Honda.Start_Engine()
Honda.Transmission_Type()
Honda.Person_Driving()
Honda.Max_Speed()
Honda.Stop_Engine()


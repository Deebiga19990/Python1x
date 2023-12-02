class Car:
    def __init__(self,model,make):
        self.make=make
        self.model=model
        print("Constructor called")
    def start(self):
        print("start", self.make,self.model)

car1=Car("Toyato","Camry")
car1.start()
car2=Car("Honda","self")


car2.start()

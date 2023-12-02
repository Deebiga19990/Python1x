class Car:
    name = None
    color = None
    model = None
    speed = None
    engine = None

    def start_engine(self):
        print("Start Engine\n")

    def person_driving(self):
        print("Im driving "+ self.name)

Tesla_Obj=Car()
Lambo_Obj=Car()


Tesla_Obj.name="Tesla"
Lambo_Obj.name="Lambo"

Tesla_Obj.person_driving()
Lambo_Obj.person_driving()


class Car():
    nangu='ffgfgfgf'
    def __init__(self,name,mileage,engine,BHP,transmission):
        self.name=name
        self.mileage=mileage
        self.engine=engine
        self.BHP=BHP
        self.transmission=transmission

class SportsCar(Car):
    def __init__(self,name,mileage,engine,BHP,transmission,top_speed):
        Car.__init__(self,name,mileage,engine,BHP,transmission)
        self.top_speed=top_speed
class SUV(Car):
    def __init__(self,name,mileage,engine,BHP,transmission,seat_capacity):
        Car.__init__(self,name,mileage,engine,BHP,transmission)
        self.seat_capacity=seat_capacity
aa=Car("Dc Avanti","10.0 kmpl","1998 cc","310.0","Manual")
print(aa.name)
print(aa.mileage)
print(aa.engine)
print(aa.BHP)
print(aa.transmission)
bb=SportsCar("Dc Avanti","10.0 kmpl","1998 cc","310.0","Manual","350kmps")
print(bb.name)
print(bb.mileage)
print(bb.engine)
print(bb.BHP)
print(bb.transmission)
print(bb.top_speed)
cc=SUV("Dc Avanti","10.0 kmpl","1998 cc","310.0","Manual","extra comfort")
print(cc.name)
print(cc.mileage)
print(cc.engine)
print(cc.BHP)
print(cc.transmission)
print(cc.seat_capacity)
# 1. Create Vehicle class with max_speed and milege attributes
class Vehicle:
    def __init__(self,mx_speed,milege):
        self.mx_speed = mx_speed
        self.milege = milege

ns200 = Vehicle(120,40)

print(ns200.mx_speed)

# 2. Create Vehicle class without any variables or method
class Vehicle:
    pass

# 3. Create child class Bus that will inherit all the variable and methods from vehicle class.
class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    pass

vandi = Bus('school vandi','60','20')
print(vandi.name)

# 4.Create a Bus class that inherits from the Vehicle class. 
# Give the capacity argument of Bus.seating_capacity() a default value of 50.

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_cap(self, capacity=50):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

class Bus(Vehicle):
    def seating_cap(self, capacity=50):
        return super().seating_cap(capacity)


vandi = Bus('school vandi','60','20')
carvandi = Vehicle('clg vandi','55','25')
print(vandi.seating_cap())
print(carvandi.seating_cap(20))

class Sample:
    def sam(self,dummy):
        return('this is sample '+ dummy)

summa= Sample()
print(summa.sam('aji'))


class Marks:
    def __init__(self,mat,phy,che):
        self.mat=mat
        self.phy=phy
        self.che=che
    
    def total(self):
        tot=self.mat+self.phy+self.che
        return tot

ajith = Marks(120,188,130)
print(ajith.total)
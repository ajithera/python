#Excersise-1
'''
Create a class, Triangle. Its __init__() method should take self, angle1, angle2, and angle3 as arguments. Make sure to set these appropriately in the body of the __init__()method.
Create a variable named number_of_sides and set it equal to 3.
Create a method named check_angles. The sum of a triangle's three angles is It should return True if the sum of self.angle1, self.angle2, and self.angle3 is equal 180, and False otherwise.
Create a variable named my_triangle and set it equal to a new instance of your Triangle class. Pass it three angles that sum to 180 (e.g. 90, 30, 60).
Print out my_triangle.number_of_sides and print out my_triangle.check_angles().
'''
class Triangle:
    number_of_sides = 3
    def __init__(self,ang1,ang2,ang3):
        self.ang1=ang1
        self.ang2=ang2
        self.ang3=ang3
    
    def check_angles(self):
        sum = self.ang1+self.ang2+self.ang3
        if sum == 180:
            return True
        else :
            return False

my_triangle = Triangle(90,60,30)
print(my_triangle.number_of_sides)
print(my_triangle.check_angles())

class Marks:
    def __init__(self,maths,phy,chem):
        self.math = maths
        self.phy = phy
        self.chem=chem

    def cutoff(self):
        cutoff = (self.math + self.phy + self.chem)/3
        return cutoff
    

ajith = Marks(120,186,140)
print(ajith.cutoff())
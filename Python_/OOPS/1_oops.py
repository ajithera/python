#class - like blue print
#object - Created using class
#methods - functions inside the class
#Self - Instance variable used to hold the object name

#example - 1
class Student:
    pass

stu1=Student()
stu2=Student()

print(type(stu1))
print(stu2)


stu1.name='ajith'
stu1.rollno='001'
stu1.dob='Aug-96' 

stu2.name='Vijay'
stu2.rollno='002'
stu2.dob='Aug-97'

print(stu1.name)

stu1_ = {'name':'ajith','rollno':'001','dob':'Aug-96'}
print(stu1_['name'])

#the above method took more code to put values into variables
#to reduce this we go for '__init__' method (this is called constructor in other languages)

#example-2
from datetime import date
class Student:
    #this is init method( this is initialise the class)
    def __init__(self,name,rollno,dob):  #these are the values we give at run time
        self.name=name
        self.rollno=rollno
        self.dob=dob

#self - instance variable
#It instantly holds the object name
    def address(self):
        addr= f"name : {self.name}\nrollno:{self.rollno}\ndob : {self.dob}"
        return addr
    
    def age(self):
        current_year=date.today().year
        return current_year-self.dob
# In this self represents the object (i.e -> self.name => stu1.name)

stu1=Student('ajith','001',1996)
stu2=Student('vijay','002','1997')

print(stu1.name)
print(stu1.age())
print(stu2.address())

#Class variable
#Class variable is variable we can create for overall class

#Rule 1 - if we use class variable class level inside any method we should mention the class name like class_name.class_variable.
#Rule 2 - If methods have any attributes then we should not use 'return' keyword.It wont work either.


#For example 2, It has name,rollno,dob attributes. Now we need to add one more attribute called 'fees'
#'fees' is common for all students. Now we can create this variable by below

#way-1
#manually giving attribute to each object level.
stu1.fee=10000
stu2.fee=10000

#way-2
#if we give attribute to class level it will automatically taken into object level
Student.fee=20000

print(stu1.fee)

#to create class variable in class
#class variable should be inside class and outside of method
#In example-2
from datetime import date
class Student:
    fee=20000 #class variable

    #this is init method( this is initialise the class)
    def __init__(self,name,rollno,dob):  #these are the values we give at run time
        self.name=name
        self.rollno=rollno
        self.dob=dob

#self - instance variable
#It instantly holds the object name
    def address(self):
        addr= f"name : {self.name}\nrollno:{self.rollno}\ndob : {self.dob}"
        return addr
    
    def age(self):
        current_year=date.today().year
        return current_year-self.dob

stu1=Student('ajith','001',1996)
stu2=Student('vijay','002','1997')

print(stu1.fee)  #it returns the class variable value 20000

#we want change the fee of stu1

stu1.fee=15000

print(stu1.fee)
#this will give the value 15000
#that does not mean it changed the value of class variable

print(Student.fee) #2000

#So whenever we change the class variable for any object, one instance variable is created for that object 
#..with the same name of class variable name.

#to check the instance variable created for the object python has one special attribute called '__dict__'
print(Student.__dict__)
print(stu1.__dict__)
#Here 'fee' instance variable is created bcz we changed the fee for this obj.

print(stu2.__dict__)
#Here there is no variable called 'fee'

#But we can see the fee value for 'stu2'. This value is taken from class variable
print(stu2.fee) #20000

#now we need add one method called pay_fees.
#and find how many objects were created using class.
class Mech_dept:
    fee = 20000
    no_of_obj = 0 #initially we need put this as 0
    def __init__(self,name,rollno,dob):
        self.name=name
        self.rollno=rollno
        self.dob=dob
        Mech_dept.no_of_obj = Mech_dept.no_of_obj + 1 #This will add one whenver the obj is created using this class

    def age(self):
        age=2021- self.dob
        return age

    def pay_fee(self,amount):
        self.fee = self.fee - amount


stu1=Mech_dept('ajith','001',1996)
stu2=Mech_dept('vijay','002','1997')
stu1.pay_fee(5000)

print(stu1.fee) #check the remaining fee

print(Mech_dept.no_of_obj) #check the number of obj created using the class

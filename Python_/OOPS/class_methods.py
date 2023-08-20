class Student:
    country = 'india'
    state='tn'
    def __init__(self,name,tot):
        self.name=name
        self.tot=tot
    
    #instance method
    def ins(self):
        print('Hi ',self.name)
 
    #class method
    @classmethod
    def cls(cls):
        print('the country is ',cls.country)
        print('the state is ',cls.state)
    
    #static method
    @staticmethod
    def stat():
        print('this is static')
    
    def ins_stat(self):
        stat='this is method variable'
        print(stat,self.name)
    
    # @classmethod              --it wont work
    # def ins_cls(cls,self):
    #     print(self.name,cls.country)

a = Student('ajith',200)
a.ins()
a.cls()
a.stat() 

Student.stat()
Student.cls()


a.ins_stat()

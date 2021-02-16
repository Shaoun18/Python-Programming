# 1st code
'''
class student :                                  # class declr
    roll = ""
    gpa = ""

    def __init__(self,roll,gpa):                       # constructor define
        self.roll = roll
        self.gpa = gpa

    def set_value(self):
        print(f"roll : {self.roll}, gpa :{self.gpa}")

karim =  student(101,3.5)                                 # object
karim.set_value()

rahim =  student(102,3.7)
rahim.set_value()
'''

# 2nd code

class Triangle :

    def set_variable(self,base,height):
        self.height = height
        self.base = base

    def calculate_area(self):
        area = .5 * self.base * self.height
        print("Area = ",area)

t1 = Triangle()
t1.set_variable(10,20)
t1.calculate_area()
t2 = Triangle()
t2.set_variable(20,30)
t2.calculate_area()

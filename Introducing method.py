class student :                                   # class declr
    roll = ""
    gpa = ""

    def set_variable(self,roll,gpa):                       # function decl
        self.roll = roll
        self.gpa = gpa

    def set_value(self):
        print(f"roll : {self.roll}, gpa :{self.gpa}")

karim =  student()                                 # object
karim.set_variable(101,3.5)                       # function call
karim.set_value()

rahim =  student()
rahim.set_variable(102,3.7)
rahim.set_value()
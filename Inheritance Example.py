class shape :
    def __init__(self,dim1,dim2):
        self.dim1 = dim1
        self.dim2 = dim2

    def area(self):
        print("Enter the area of : ")

class Triangle(shape):                             # inheritate the program
    def area(self):
        area = .5 * self.dim1 * self.dim2
        print("Area of Triangle : ",area)

class Rectangle(shape):
    def area(self):
        area = self.dim1 * self.dim2
        print("Area of Rectangle : ",area)

t1 = Triangle(20,30)
t1.area()

r1 = Rectangle(20,30)
r1.area()
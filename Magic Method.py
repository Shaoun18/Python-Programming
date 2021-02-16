class Bike :
    def __init__(self,name,color):
        self.name = name
        self.color = color

    def __eq__(self, other):                                   # Magic Method Apply
        return self.name == other.name and self.color == other.color

    def __str__(self):                                        # Magic Method Apply
        return (f"Name = {self.name},color = {self.color}")

    def display(self):
        print(f"Name = {self.name},color = {self.color}")

bike1 = Bike("yamma R15","Blue")
bike2 = Bike("yamma R15","Blue")
print(bike1 == bike2)                     # equal Method Apply
print(str(bike2))                         # string Method Apply
print(str(bike1))
class Dog() :
    
    def _init_(self, name, age):
        self.name = name
        self.age = age

    def sit(self):
        print(self.name.tittle() + "is now sitting")

    def roll_over(self):
        print(self.name.tittle() + "rolled over!")
        
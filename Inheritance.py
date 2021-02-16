class phone:
    def call(self):
        print("You take a Call")
    def messege(self):
        print("you take a messege")

class samsung(phone):                 # inherite the class
    # call ,messege define
    def photo(self):
        print("You take a photo")

s = samsung()
s.photo()
s.call()
s.messege()
print(issubclass(samsung,phone))
print(issubclass(phone,samsung))
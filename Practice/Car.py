class car ():

    def _init_(self, make, model, year) :
        self.make = make
        self.model = model 
        self.year = year 

    def get_descriptive_name (self):
        long_name = str(self.year) + '' + self.make + self.model 
        return long_name.title()

    def read_odometer(self):
        print('This car has ' + str(self.odometer_reading) + "miles on it.")

    my_new_car = car('audi', 'a4', 2016)
    print (my_new_car.get_descriptive_name())

    my_new_car.read_odometer()


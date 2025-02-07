# object oriented programming
class Car:
    # constructor method
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
     # a method function
    def describe_car(self):
        print(f"My dream car make :{self.make}, "
               f"\nMy dream car model:{self.model}"
              f"manufacturer:{self.year}")
# create object or instances of a class
myobj = Car("toyota","lexus",2024)
myobj.describe_car()
myobj2 = Car("toyota","prado",2023)
myobj2.describe_car()
myobj3 = Car("Audi","audi SQ5",2025)
myobj3.describe_car()
myobj4 = Car("jeep","wagon",2022)
myobj4.describe_car()
myobj5 = Car("bmw","mercedes", 2024)
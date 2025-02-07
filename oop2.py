# create a clss called fruits that has the following attributes name colour cost
# impliment a constructor method and a method function that prints:"myfavourite fruit is ___, color___,cost"
# create five instance of that class
class fruits:
    # constructor method
    def __init__(self, name ,color, cost):
        self.name = name
        self.color = color
        self.cost = cost
    # a method function
    def describe_fruits(self):
        print(f"My favourite fruit:{self.name},"
              f"My favourite fruit color:{self.color}"
              f"My favourite fruit cost:{self.cost}")
# create instances of a class
myfruit = fruits("banana","yellow",20)
myfruit.describe_fruits()
myfruit2 = fruits("apple","red",50)
myfruit2.describe_fruits()
myfruit3 = fruits("avocado","green",40)
myfruit3.describe_fruits()
myfruit4 = fruits("watermelon","red and green",140)
myfruit4.describe_fruits()
myfruit5 = fruits("orange","orange",20)
myfruit5.describe_fruits()
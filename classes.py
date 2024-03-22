class Home:
    def __init__(self, sqft, location, home_rate):
        self.sqft = sqft
        self.location = location
        self.rate = home_rate
        # setting default values without arguments
        self.flooring = 'marble'
        print("Home object created")

    def painting(self, paint_rate):
        self.paint_rate = paint_rate
        print(f"Price for painting: {self.sqft * self.paint_rate}")
        print("Painting done")

    def main_gate_automation(self):
        print("Main Gate automation done")

class TennisCourt:
    def __init__(self):
        self.floor = 'turf'
        print("Tennis Court object created")

class Apartment(Home):
    def __init__(self, sqft, location, home_rate, society):
        super().__init__(sqft, location, home_rate)
        self.society = society
        # Creating another instance as attribute
        self.tennis_court = TennisCourt()
        print("Apartment object created")

    # There is no main gate for an apartment flat, so overriding
    def main_gate_automation(self, price):
        print("No Main Gate for a Apartment flat")

my_home = Home(900, "Anna Nagar", 10000)
print(my_home.sqft)
print(f"My home floor is {my_home.flooring}")
my_home.painting(100)

my_apt = Apartment(900, "Anna Nagar", 10000, "Kumar Kruti")
my_apt.painting(120)
print(my_apt.sqft)

my_home.main_gate_automation()
# even though below overriden method has different argument than partent class,
#   still it will override
my_apt.main_gate_automation(12000)

# accessing partent class attributes is same as self
print(my_apt.location)
# accessing instances created in object is as follows
print(my_apt.tennis_court.floor)


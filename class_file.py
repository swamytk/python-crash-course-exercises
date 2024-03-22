# This python file is used to learn pytest. Refer classes.py to learn functions in classes

class HomeClass:
    def __init__(self, sqft, location, home_rate):
        self.sqft = sqft
        self.location = location
        self.rate = home_rate
        # setting default values without arguments
        self.flooring = 'marble'
        print("Home object created")

    def get_home_price(self):
        return self.sqft * self.home_rate

# There is a bug here. The home_rate & sqft can't be <= zero, 
#   which is not handled in this class

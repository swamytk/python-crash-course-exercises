from random import randint

class Die:
    ''' A class to implement a Die '''

    def __init__(self, num_sides=6):
        self.num_sides = num_sides
    
    def roll(self):
        ''' return a random value between 1 and num_sides '''
        return randint(1, self.num_sides)

        
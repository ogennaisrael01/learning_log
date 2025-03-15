from random import randint
class Dice():
    def __init__(self, sides=6):
        self.sides = sides

    def roll_dice(self):
        rolled_side = randint(1, self.sides)
        print(rolled_side)

dice = Dice(20)
dice.roll_dice()
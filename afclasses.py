import random

class Items:
    def __init__(self):
        self.inventory
        self.consumable

class Narrator():
    def __init__(self):
        self.storyteller = {}
        pass

class DialogueTree():
    def __init__(self):
        self.savestates = {}
    def add_savestate(self, choice, outcome):
        self.savestates[choice] = outcome

class Npc:
    def __init__(self, cutesy, tricksy, sneaksy, meany, fasty, mightsy):
        self.cutesy = cutesy
        self.tricksy = tricksy
        self.sneaksy = sneaksy
        self.meany = meany
        self.fasty = fasty
        self.mightsy = mightsy
        pass

    def cutesy_dice_roll(self):
        roll = [random.randint(1,6) for x in range(self.cutesy)]
        return roll
    def sneaksy_dice_roll(self):
        roll = [random.randint(1,6) for x in range(self.sneaksy)]
        return roll
    def meany_dice_roll(self):
        roll = [random.randint(1,6) for x in range(self.meany)]    
        return roll
    
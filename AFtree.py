#Animal Forest Dialogue
import random

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
    
class Squirrel(Npc):
    def __init__(self,cutesy, tricksy, sneaksy, meany, fasty, mightsy):
        super().__init__(cutesy, tricksy, sneaksy, meany, fasty, mightsy)
        self.dialogue = {
            'intro1': '\nSquirrel: "Deal but i get my half now!"',
            'intro2': '\nSquirrel: "Is that...is that honey...?"',
            'intro3': 'Squirrel: "But...but...oh okay.." *sniff* *sniff*',
            'intro4': 'Squirrel: "No! NO! I eat it all now!" ***SQUIRREL RAGE***',
            'intro5': 'Squirrel: "Maybe, I still have things to bury"',
            'intro6': 'Squirrel: "I have to help bury more things today anyways."',
            'intro7': 'Squirrel: "I see it. I seet it. Its honey in that leaf!"\
***Eyes turn red SQUIRREL RAGE***'
        }
        pass


class Opossum(Npc):
    def __init__(self, cutesy, tricksy, sneaksy, meany, fasty, mightsy):
        super().__init__(cutesy, tricksy, sneaksy, meany, fasty, mightsy)
        self.dialogue = {
            'intro1': '\nOPOSSUM: "So you\'re really going to go into town?"'
        }
        pass


class Raccoon(Npc):
    def __init__(self, cutesy, tricksy, sneaksy, meany, fasty, mightsy):
        super().__init__(cutesy, tricksy, sneaksy, meany, fasty, mightsy)
        self.dialogue = {
            'intro1':'\nRACCOON: "Yea, and I was hoping you two come with me...\
I asked my uncle, he says its not against the rules.\
 Just that I have to be the one to actually get it."'            
        }
        pass


    def introdiag_choice(self):
        
        print('\n1) Raccoon: "It is! And we can all share the honey.\
If not, then its just me. But I\'ll be alone with all this honey"')
        
        print('\n2) Raccoon: "There\'s no honey...what are you talking about?"')

        print('\n3) Raccoon: "It\'s for me, but i will let you sniff it along the way."')
        
        introdiag_choice_made = int(input("Choose 1, 2, or 3: "))
        if introdiag_choice_made == 1:
            
            roll = raccoon1.cutesy_dice_roll()
            success = sum(1 for die in roll if die >= squirrel1.cutesy)
            print(success)
            if success >= 2:
                success = squirrel1.dialogue['intro1'] 
                print(raccoon1.cutesy_dice_roll())
                print(success)
                success = True
                dialogue.add_savestate(introdiag_choice_made, success)
            else:  
                failure = squirrel1.dialogue['intro5']
                print(failure)
                failure = False
                dialogue.add_savestate(introdiag_choice_made, failure)    
        elif introdiag_choice_made == 2:
            roll = raccoon1.sneaksy_dice_roll()            
            success = sum(1 for die in roll if die >= squirrel1.sneaksy)
            if success >= 2:
                success = squirrel1.dialogue['intro6']
                print(success)
                success = True
                dialogue.add_savestate(introdiag_choice_made, success)
            else:
                failure = squirrel1.dialogue['intro7']
                print(failure)
                failure = False
                dialogue.add_savestate(introdiag_choice_made, failure)
        else:
            roll = raccoon1.meany_dice_roll()            
            success = sum(1 for die in roll if die >= squirrel1.meany)
            if success >= 2:
                success = squirrel1.dialogue['intro3']
                print(success)
                success = True
                dialogue.add_savestate(introdiag_choice_made, success)
            else:
                failure = squirrel1.dialogue['intro4']
                print(failure)
                failure = False
                dialogue.add_savestate(introdiag_choice_made, failure)

dialogue = DialogueTree()
opossum1 = Opossum(3, 2, 4, 4, 1, 4)
raccoon1 = Raccoon(3, 5, 3, 2, 3, 3)
squirrel1 = Squirrel(4, 3, 2, 5, 5, 1)

def introdialogue():


     print(opossum1.dialogue['intro1'])
     print(raccoon1.dialogue['intro1'])
     print(squirrel1.dialogue['intro2'])
     raccoon1.introdiag_choice()

introdialogue()
print(dialogue.savestates)


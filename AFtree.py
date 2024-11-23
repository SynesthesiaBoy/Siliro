#Animal Forest Dialogue
import random
from afclasses import *



   
    
class Squirrel(Npc):
    def __init__(self,cutesy, tricksy, sneaksy, meany, fasty, mightsy):
        super().__init__(cutesy, tricksy, sneaksy, meany, fasty, mightsy)
        self.dialogue = {
            'intro1': '\nSquirrel: "Deal! Deal! But i get my half now!" ***CHOMP CHOMP***',
            'intro2': '\nSquirrel: "Is that...is that honey...?"',
            'intro3': '\nSquirrel: "But...but...oh okay.." *sniff* *sniff*',
            'intro4': '\nSquirrel: "No! NO! I eat it all now!" ***SQUIRREL RAGE***',
            'intro5': '\nSquirrel: "But going into town? This stick, it\'s important, but maybe not \
as important as burying things so I can lose them- I mean use them later."',
            'intro6': '\nSquirrel: "I...I thought..hmm...Fine, but we need to find something \
yummy there"',
            'intro7': '\nSquirrel: "I see it. I seet it. Its honey in that leaf!"\
***Eyes turn red SQUIRREL RAGE***'
        }
        self.item_list = []
        pass


class Opossum(Npc):
    def __init__(self, cutesy, tricksy, sneaksy, meany, fasty, mightsy):
        super().__init__(cutesy, tricksy, sneaksy, meany, fasty, mightsy)
        self.dialogue = {
            'intro1': '\nOPOSSUM: "So you\'re really going to go into town?"',
            'intro2': '\nOPOSSUM: "I-I-I\'m-I don\'t know, those people-folk are sc-scary."',
            'intro3': '\nOPOSSUM: "I\'m too scared, I just slow you down. I feel...useless. \
You know how my kin get. All the cheese and trash can\'t change that.'
        }
        
        self.item_list = []
        pass


class Raccoon(Npc):
    def __init__(self, cutesy, tricksy, sneaksy, meany, fasty, mightsy):
        super().__init__(cutesy, tricksy, sneaksy, meany, fasty, mightsy)
        self.dialogue = {
            'intro1':'\nRACCOON: "Yea, and I was hoping you two come with me...\
I asked my uncle, he says its not against the rules.\
 Just that I have to be the one to actually get it."',
            'intro2': '\nRACCOON: "Come on Opposum! Even Aunty Possum sneaks there. \
How do you think she gets us those cheese treats? And think of the trash!'            
        }
        
        self.item_list = []


    def introdiag_choice(self):
        
        print('\n1) Raccoon: "It is! And we can all share the honey.\
If not, then its just me. But I\'ll be alone with all this honey"')
        
        print('\n2) Raccoon: "There\'s no honey...what are you talking about?"')

        print('\n3) Raccoon: "It\'s for me, but i will let you sniff it along the way."')
        
        introdiag_choice_made = int(input("Choose:\n1)\n2)\n3)\n->"))
        if introdiag_choice_made == 1:
            
            roll = raccoon1.cutesy_dice_roll()
            success = sum(1 for die in roll if die >= squirrel1.cutesy)
            print(success)
            
            if success >= 2:
                print(squirrel1.dialogue['intro1']) 
                print(raccoon1.cutesy_dice_roll())
                dialogue.add_savestate(introdiag_choice_made, True)
            else:  
                print(squirrel1.dialogue['intro5'])
                dialogue.add_savestate(introdiag_choice_made, False)  

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

    def intro2diag_choice(self):
        
        print('\n1) RACCOON: "If Aunty Possum can do it, so can you. You\'re the \
most bravest one here. You just don\'t know it yet."')

        print('\n2) RACCOON: "The cheese tasting phase of your life won\'t \
start while feeling sorry for yourself. Go on then, more cheese and trash for me."')

        print('\n3) RACCOON: "A little birdy told me about a nice pile of trash. Just \
for you."')
        intro2diag_choice_made = int(input("Choose:\n1)\n2)\n3)\n->"))
        
dialogue = DialogueTree()
opossum1 = Opossum(3, 2, 4, 4, 1, 4)
raccoon1 = Raccoon(3, 5, 3, 2, 3, 3)
squirrel1 = Squirrel(4, 3, 2, 5, 5, 1)

def introdialogue():


     print(opossum1.dialogue['intro1'])
     print(raccoon1.dialogue['intro1'])
     print(squirrel1.dialogue['intro2'])
     raccoon1.introdiag_choice()
def intro2dialogue():
    print(opossum1.dialogue['intro2'])
    print(raccoon1.dialogue['intro2'])
    print(opossum1.dialogue['intro3'])
    raccoon1.intro2diag_choice()
introdialogue()
intro2dialogue()
print(dialogue.savestates)


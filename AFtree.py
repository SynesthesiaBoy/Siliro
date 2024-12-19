#Animal Forest Dialogue
import random

class Items:
    def __init__(self):
        self.inventory
        self.consumable

class Narrator():
    def __init__(self):
        self.story = {
                'intro1': '\nNARRATOR: "Our three young furry friends met at their favorite tree, \
in their favorite forest. Well, maybe not their favorite tree, it was \
an okay tree. But technically it WAS their favorite forest. I mean \
it was the ONLY forest they knew. The point is, they were there and about to do something epic. \
An incredible journey full of...cheese? Is this right? Just read the- You\'re not even paying \
me. So they\'re really going into town?"\n',
                      'intro2': '\nNARRATOR: "The oppossum felt gassy....*sigh*...I\'m going to be\
 saying that a lot...',
                    'intro3': '\nNARRATOR: "The sound broke wind, pun intended. We intend puns here\
. The wind reverberated far enough to tickle the ear of a nearby raptor. An alarm in the forest \
went out, one that could only be deciphered by the most pompous of birds. Great myths and legends \
are often written about in books long ago weathered. While enjoying the night beginning, a great horned owl appeared!\
 It swooped in and gripped a branch nearby. Our furry friends darted behind clumps of leaves.',
                    'owlencounter2': '\nNARRATOR: "The great horned owl flapped it\'s wings. At this point\
 he decided to play with his food."',
                    'owlencounter1': '\nNARRATOR: "The squirrel and raccoon knew what would come next. \
Not often where they under the watch of a great owl. Especially one that could make them meet the after realms. \
The oppossum, struck with fear, reluctantly squeezed out another from behind her hiding spot. \
The squirrel and raccoon remained paralyzed, too tense to move. The large predator let out a similar answer, \
with it\'s own wind."'
        }

storyteller = Narrator()
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
    def tricksy_dice_roll(self):
        roll = [random.randint(1,6) for x in range(self.tricksy)]   
        return roll 
    def fasty_dice_roll(self):
        roll = [random.randint(1,6) for x in range(self.fasty)]   
        return roll 
    def mightsy_dice_roll(self):
        roll = [random.randint(1,6) for x in range(self.mightsy)]   
        return roll 

   
    
class Squirrel(Npc):
    def __init__(self,cutesy, tricksy, sneaksy, meany, fasty, mightsy):
        super().__init__(cutesy, tricksy, sneaksy, meany, fasty, mightsy)
        self.rage = False
        self.dialogue = {
            'intro1': '\nSquirrel: "Deal! Deal! But i get my half now!" ***CHOMP CHOMP***',
            'intro2': '\nSquirrel: "Is that...is that honey...?"',
            'intro3': '\nSquirrel: "But...but...oh okay.." *sniff* *sniff*',
            'intro4': '\nSquirrel: "No! NO! I eat it all now!" ***SQUIRREL RAGE***',
            'intro5': '\nSquirrel: "But going into town? This stick, it\'s important, but maybe not \
as important as burying things so I can lose them- I mean use them later."',
            'intro6': '\nSquirrel: "I...I thought..hmm...Fine, but we need to find something \
yummy there."',
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
You know how my kin get. All the cheese and trash can\'t change that.',
            'intro4': '\nOPOSSUM: "O-okay, I can try. But we have to come up with a plan."',
            'intro5': '\nOPOSSUM: "Her stories are great n\' all, but we might get l-lost!"',
            'intro6': '\nOPOSSUM: "I=I will show you! I think we got this...***RUMBLE RUMBLE***not again..."',
            'intro7': '\nOPOSSUM: "Y-you can\'t push us around like that RACCOON, all the \
cheese in the world won\'t make anyone like you. It\'s also upsetting my tummy..."',
            'intro8': '\nOPOSSUM: "succeess3"',
            'intro9': '\nOPOSSUM: "And how did you do that if its our first time going there?"',
            'poot': '\n***POOT!***'
        }
        
        self.item_list = []
        pass

class Owl(Npc):
    def __init__(self, cutesy, tricksy, sneaksy, meany, fasty, mightsy):
        super().__init__(cutesy, tricksy, sneaksy, meany, fasty, mightsy)
        self.dialogue = {
            'hootapoot1': '\nOWL: "You *HOOT* yet no who that I knooow. Does the food speak?"',
            'hootapoot2': '\nOWL: "You poot at me and I hoot at you. I will poot on you can you\
 hoot at me?',
            'hootapoot3': '\nOWL: ***HOO*** ***HOO*** ***HOO*** "could think food could think!"',
            'hootapoot4': '\nOWL: "O',
            'hoot': '\n***Hoot*** ',
            'poot': '\n***Poot*** '
        }
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
        
        self.item_list = ['wrapped_honey']


    def introdiag_choice(self):
        
        print('\n1) Raccoon: "It is! And we can all share the honey.\
If not, then its just me. But I\'ll be alone with all this honey"')
        
        print('\n2) Raccoon: "There\'s no honey...what are you talking about?"')

        print('\n3) Raccoon: "It\'s for me, but i will let you sniff it along the way."')
        
        introdiag_choice_made = int(input("Choose:\n1)\n2)\n3)\n->"))
        if introdiag_choice_made == 1:
            
            roll = raccoon1.cutesy_dice_roll()
            success = sum(1 for die in roll if die >= squirrel1.cutesy)
            print(f"Roll: {roll} Successes: {success}")
            
            if success >= 2:
                print(squirrel1.dialogue['intro1']) 
                print(squirrel1.cutesy)
                dialogue.add_savestate(introdiag_choice_made, True)
            else:  
                print(squirrel1.dialogue['intro5'])
                print(squirrel1.cutesy)
                dialogue.add_savestate(introdiag_choice_made, False)  

        elif introdiag_choice_made == 2:
            roll = raccoon1.sneaksy_dice_roll()            
            success = sum(1 for die in roll if die >= squirrel1.sneaksy)
            print(f"Roll: {roll} Successes: {success}")

            if success >= 2:
                print(squirrel1.dialogue['intro6'])
                print(squirrel1.sneaksy)
                dialogue.add_savestate(introdiag_choice_made, True)
            else:
                print(squirrel1.dialogue['intro7'])
                squirrel1.rage = True
                print(squirrel1.rage)
                print(squirrel1.sneaksy)
                dialogue.add_savestate(introdiag_choice_made, False)
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
for you. I\'ve seen it!"')
        intro2diag_choice_made = int(input("Choose:\n1)\n2)\n3)\n->"))
        
        if intro2diag_choice_made == 1:
            intro2diag_choice_made = 4
            roll = raccoon1.cutesy_dice_roll()
            success = sum(1 for die in roll if die >= opossum1.cutesy)
            print(f"Roll: {roll} Successes: {success}")
            
            if success >= 2:
                print(opossum1.dialogue['intro4']) 
                print(opossum1.cutesy)
                dialogue.add_savestate(intro2diag_choice_made, True)
            else:  
                print(opossum1.dialogue['intro5'])
                print(raccoon1.cutesy_dice_roll())
                dialogue.add_savestate(intro2diag_choice_made, False)  

        elif intro2diag_choice_made == 2:
            intro2diag_choice_made = 5
            roll = raccoon1.meany_dice_roll()            
            success = sum(1 for die in roll if die >= opossum1.meany)
            print(f"Roll: {roll} Successes: {success}")
            if success >= 2:
                
                success = opossum1.dialogue['intro6']
                print(opossum1.meany)
                dialogue.add_savestate(intro2diag_choice_made, True)
            else:
                failure = opossum1.dialogue['intro7']
                print(opossum1.meany)
                dialogue.add_savestate(intro2diag_choice_made, False)
        else:
            intro2diag_choice_made = 6
            roll = raccoon1.tricksy_dice_roll()            
            success = sum(1 for die in roll if die >= opossum1.tricksy)
            if success >= 2:
                success = opossum1.dialogue['intro8']
                print(success)
                success = True
                dialogue.add_savestate(intro2diag_choice_made, success)
            else:
                failure = opossum1.dialogue['intro9']
                print(failure)
                failure = False
                dialogue.add_savestate(intro2diag_choice_made, failure)

        
dialogue = DialogueTree()
opossum1 = Opossum(3, 2, 4, 4, 1, 4)
raccoon1 = Raccoon(3, 5, 3, 2, 3, 3)
squirrel1 = Squirrel(4, 3, 2, 5, 5, 1)
owl = Owl(6, 6, 6, 6, 6, 6)
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
def intro3dialgue():
    print(storyteller.story['intro2'])
    print(opossum1.dialogue['poot'])
    print(storyteller.story['intro3'])
def owl_encounter():
    print(owl.dialogue['hootapoot1'])
    print(opossum1.dialogue['poot'])
    print(owl.dialogue['hootapoot2'])
    print(owl.dialogue['poot'])
    print(storyteller.story['owlencounter1'])
    print(opossum1.dialogue['poot'])
    print(owl.dialogue['hoot'])
    print(owl.dialogue['poot'])
    print(storyteller.story['owlencounter2'])

    print("""

>>>>>>>> CHOOSE ACTIONS <<<<<<<<<

1) Have the possum poot again.

2) Stay quiet. Stay low.

3) Have the squirrel create a distraction.
    """)

    owl_encounter_choice = int(input("Choose:\n1) \n2)\n3)\n->"))
    
    if owl_encounter_choice == 1:
        print('\nNARRATOR: "The only proper response seemed fitting."')
        print('\nRACCOON(whisper): "See if you can talk to it."')
        print('\nNARRATOR: "The oppossum felt gassy. And with the encouragement of the Raccoon she found strength. \
It does not give me much pleasure, and frankly I think this bit is a little over done, \
but the two pootists and hootists began to speak in a language they both understood.')
################################################
print(storyteller.story['intro1'])
introdialogue()
intro2dialogue()
intro3dialgue()
owl_encounter()

print(dialogue.savestates)

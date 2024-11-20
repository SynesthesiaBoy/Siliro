#Animal Forest Dialogue


class DialogueTree():
    def __init__(self):
        self.savestates = {}
    def add_savestate(self, choice, outcome):
        self.savestates[choice] = outcome

class Npc:
    def __init__(self):
        pass

class Squirrel(Npc):
    def __init__(self, cutesy, tricksy, sneaksy, meany):
        super().__init__()
        self.cutesy = cutesy
        self.tricksy = tricksy
        self.sneaksy = sneaksy
        self.meany = meany
        pass
    def introdiag(self):
        return '\nSquirrel: "Is that...is that honey...?"'

class Opossum(Npc):
    def __init__(self, cutesy, tricksy, sneaksy, meany):
        super().__init__()
        self.cutesy = cutesy
        self.tricksy = tricksy
        self.sneaksy = sneaksy
        self.meany = meany
        pass
    def introdiag(self):
        return '\nOPOSSUM: "So you\'re really going to go into town?"'

class Raccoon(Npc):
    def __init__(self, cutesy, tricksy, sneaksy, meany):
        super().__init__()
        self.cutesy = cutesy
        self.tricksy = tricksy
        self.sneaksy = sneaksy
        self.meany = meany
        pass

    def introdiag(self):
        return '\nRACCOON: "Yea, and I was hoping you two come with me...\
I asked my uncle, he says its not against the rules.\
Just that I have to be the one to actually get it."'

    def introdiag_choice(self):
        
        print('1) Raccoon: "It is! And we can all share the honey.\
If not, then its just me. But I\'ll be alone with all this honey"\n')
        
        print('2) Raccoon: "There\'s no honey...what are you talking about?"\n')

        print('3) Raccoon: "I will give you the entire thing if you come with us."\n')
        
        introdiag_choice_made = int(input("Choose 1, 2, or 3: "))
        if introdiag_choice_made == 1:
            outcome = 'Squirrel: "Maybe, I still have things to bury"'
            print(outcome)
        elif introdiag_choice_made == 2:
            outcome = 'Squirrel: "I see it. I seet it. Its honey in that leaf!"\
***Eyes turn red SQUIRREL RAGE***'
            print(outcome)
        else:
            print("NEED CODE FOR 'ROLLING'")
            print(outcome)
        dialogue.add_savestate(introdiag_choice_made, outcome)

dialogue = DialogueTree()
opossum1 = Opossum(3, 2, 4, 4)
raccoon1 = Raccoon(4, 5, 3, 2)
squirrel1 = Squirrel(1, 3, 2, 5)

def introdialogue():


     print(opossum1.introdiag())
     print(raccoon1.introdiag())
     print(squirrel1.introdiag())
     raccoon1.introdiag_choice()

introdialogue()
print(dialogue.savestates)
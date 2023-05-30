import random


class Hostile:

    def __init__(self):
        self.HP = None
        self.name = None
        self.dmgList = [1, 2]
        self.dmg = random.choice(self.dmgList)
        self.missList = [1, 2]
        self.miss = random.choice(self.missList)

    def p_attack(self):
        self.miss = random.choice(self.missList)
        self.dmg = random.choice(self.dmgList)
        print(self.name + "'s HP = " + str(self.HP))
        print('\nYou attack the ' + self.name)
        if self.miss == 1:
            print('Your attack missed.')
            self.dmg = 0
        else:
            print('\nThe ' + self.name + ' gets ', self.dmg, ' damage.')
            if self.dmg == max(self.dmgList):
                print('A CRITICAL HIT!')
            self.HP = self.HP - self.dmg
            if self.HP <= 0:
                print('The ', self.name, ' was killed.')
            else:
                self.dmg = random.choice(self.dmgList)

    def battle(self):
        print('You encounter a ' + self.name)
        print('\n Do you want to engage?')
        battle_engage = int(input('1. Yes\n2. No'))
        if battle_engage == 1:
            while self.HP > 0:
                attack_engage = int(input('\n1. Attack\n2. Run'))
                if attack_engage == 1:
                    self.p_attack()
                else:
                    print('You ran away.')
                    break
        else:
            print('You ran away.')


gob = Hostile()
gob.name = 'Goblin'
gob.HP = 15
gob.dmgList = [4, 5, 6, 9]
gob.missList = [1, 2, 3, 4, 5, 6]

orc = Hostile()
orc.name = 'Orc'
orc.HP = 50
orc.dmgList = [6, 7, 8, 10]

elf = Hostile()
elf.name = 'Elf'
elf.HP = 50
elf.dmgList =

gob.battle()

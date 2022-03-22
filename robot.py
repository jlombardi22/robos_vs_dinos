from weapon import Weapon


class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.weapon = Weapon(weapon='sword', attack_power=10)

    def attack(self, dinosaur):
        dinosaur = dinosaur.health
        while dinosaur > 0:
            self.weapon()
            if self.weapon:
                dinosaur -= 10
                print(dinosaur)
                print(f'{self.name} uses their {self.weapon} on {dinosaur.name}')
            else:
                print('You missed')

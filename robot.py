from weapon import Weapon


class Robot:
    def __init__(self, robo_name):
        self.robo_name = robo_name
        self.robo_health = 100
        self.weapon = Weapon(weapon='sword', attack_power=10)

    def attack(self, dino):
        self.dino = 100
        while self.dino > 0:
            if self.dino == self.attack():
                dino -= 10
            if self.robo_health == 0:
                break
            else:
                print('keep fighting!')

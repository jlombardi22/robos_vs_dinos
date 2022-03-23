

class Dinosaur:
    def __init__(self, dino_name, dino_health):
        self.dino_name = dino_name
        self.attack_power = 15
        self.dino_health = dino_health

    def attack(self, robot):
        self.robot = 100
        while self.robot > 0:
            if self.robot == self.attack():
                robot -= 10
            if self.dino_health == 0:
                break
            else:
                print('keep fighting!')
    attack(self='Chomper', robot='Roomba')

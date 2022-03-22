

class Dinosaur:
    def __init__(self, name):
        self.name = name
        self.attack_power = 15
        self.health = 100

    def dino_attack(self, robot):
        robot = robot.health
        while robot > 0:
            self.attack_power()
            if self.attack_power:
                robot -= 15
                print(robot)
                print(
                    f'{self.name} uses their attack{self.attack_power} on {robot.name}')
                break
            else:
                print('You missed')

#dino_one = Dinosaur('Chomper')
# print(dino_one.name)

# def attack(self, robot):
#     robot = Robot(name='Petri').health
#     while robot > 0:
#         robot -= 10
#         print(robot)


# attack(self='Petri', robot='Terminator')

from fleet import Fleet
from herd import Herd


class Battlefield:
    def __init__(self) -> None:
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        pass

    def display_welcome(self):
        pass

    def battle(self):
        pass

    def dino_turn(self):
        user_input = input('Which dino first? <Press 1, 2, or 3>')
        if int(user_input) == 1:
            self.show_dino_opponent_options()
            pass

    def robo_turn(self):
        pass

    def show_dino_opponent_options(self):
        robot_army = Fleet()
        for robo in robot_army.robots:
            print(robo.name)

    def show_robo_opponent_options(self):
        dino_army = Herd()
        for dino in dino_army.dinosaurs:
            print(dino.name)

    def display_winners(self):
        pass

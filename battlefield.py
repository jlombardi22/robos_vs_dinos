from fleet import Fleet
from herd import Herd


class Battlefield:
    def __init__(self) -> None:
        self.fleet = Fleet()
        self.herd = Herd()

    def run_game(self):
        self.battle()

    def display_welcome(self):
        pass

    def battle(self):
        self.fleet.create_fleet(
            rob_one='Roomba', rob_two='Terminator', rob_three='Prime')
        self.herd.create_herd(
            din_one='Spike', din_two='Petri', din_three='Chomper')

    def dino_turn(self):
        user_input = input('Which dino first? <Press 1, 2, or 3>')
        if int(user_input) == 1:
            self.herd.din_one
        elif int(user_input) == 2:
            self.herd.din_two
        elif int(user_input) == 3:
            self.herd.din_three
        else:
            print('Please enter a number between 1 & 3')

    def robo_turn(self):
        user_input = input('Which robo first? <Press 1, 2, or 3>')
        if int(user_input) == 1:
            self.fleet.robot_one
        elif int(user_input) == 2:
            self.fleet.robot_two
        elif int(user_input) == 3:
            self.fleet.robot_three
        else:
            print('Please enter a number between 1 & 3')

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

from robot import Robot


class Fleet:
    def __init__(self):
        self.robots = []
        for robo in self.robots:
            print(robo)

    def create_fleet(self):
        self.robot_one = self.robots.append(Robot(name='Terminator'))
        self.robot_two = self.robots.append(Robot(name='Roomba'))
        self.robot_three = self.robots.append(Robot(name='Prime'))

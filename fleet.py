from robot import Robot


class Fleet:
    def __init__(self):
        self.robots = []

    def create_fleet(self, rob_one, rob_two, rob_three):

        self.robots.append(Robot(rob_one))
        self.robots.append(Robot(rob_two))
        self.robots.append(Robot(rob_three))

        # self.robot_one = self.robots.append(Robot(name='Terminator'))
        # self.robot_two = self.robots.append(Robot(name='Roomba'))
        # self.robot_three = self.robots.append(Robot(name='Prime'))

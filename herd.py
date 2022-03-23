from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dinosaurs = []

    def create_herd(self):
        self.din_one = self.dinosaurs.append(Dinosaur(name='Terminator'))
        self.din_two = self.dinosaurs.append(Dinosaur(name='Roomba'))
        self.din_three = self.dinosaurs.append(Dinosaur(name='Prime'))

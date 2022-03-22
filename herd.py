from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dinosaurs = []

    def create_herd(self, din_one, din_two, din_three):
        self.dinosaurs.append(Dinosaur(din_one))
        self.dinosaurs.append(Dinosaur(din_two))
        self.dinosaurs.append(Dinosaur(din_three))


# print(dinos.dinosaurs.append(dinos.create_herd(Dinosaur('Chomper'))))
# self.dino_one = self.dinosaurs.append(Dinosaur('Chomper'))
# self.dino_two = self.dinosaurs.append(Dinosaur('Blue'))
# self.dino_three = self.dinosaurs.append(Dinosaur('Petri'))

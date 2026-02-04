import random 
from Enemy import Enemy

class Zombie(Enemy):

    def __init__(self):
        super().__init__("Zombie")
    
        self.degat = random.choice([1, 2])
        self.loot = random.choice([0.5, 1])

    def attack(self):
        return f"{self.name} stabs quickly and deals {self.degat} damage!"

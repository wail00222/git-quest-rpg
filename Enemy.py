import random
from abc import ABC, abstractmethod

class Enemy(ABC):

    def __init__(self, name):
        self.name = name
        self.degat = random.choice([1, 2])
        self.loot = random.choice([0.5, 1])

    def get_degat(self):
        return self.degat
    
    def get_loot(self):
        return self.loot

    @abstractmethod
    def attack(self):
        pass
import random 

class Enemy: 
    def __init__(self):
        self.degat = random.choice([1, 2])
        self.loot = random.choice([0.5, 1])
    

    def get_degat(self):
        return self.degat
    
    def get_loot(self):
        return self.loot
    
    def attack(self):
        return f"attacks with a damage of {self.degat}!"

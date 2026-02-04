import random

class Unit:
    def __init__(self, name, unit_type, damage_range, luck, flee, price):
        self.name = name
        self.unit_type = unit_type
        self.damage_range = damage_range  
        self.luck = luck
        self.flee = flee
        self.price = price

    def get_damage(self):
        """Calcule un dégât aléatoire au moment de l'attaque."""
        return random.choice(self.damage_range)

    def __str__(self):
        return f"{self.unit_type.capitalize()} {self.name} | Prix: {self.price}"
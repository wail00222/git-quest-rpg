class Orc(Enemy):

    def __init__(self):
        super().__init__("Orc")
        # Définition des attributs spécifiques à l'Orc
        self.degat = random.choice([3, 4, 5])
        self.loot = random.choice([2, 2.5])

    def attack(self):
        return f"{self.name} swings his axe and deals {self.degat} damage!"
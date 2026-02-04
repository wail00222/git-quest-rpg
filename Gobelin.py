class Gobelin(Enemy):

    def __init__(self):
        super().__init__("Gobelin")
        # Définition des attributs spécifiques au Gobelin
        self.degat = random.choice([2, 3])
        self.loot = random.choice([1, 1.5])

    def attack(self):
        return f"{self.name} stabs quickly and deals {self.degat} damage!"
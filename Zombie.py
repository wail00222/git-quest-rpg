
class Zombie(Enemy):
    def __init__(self, name="Zombie", health=50, attack_power=10):
        super().__init__(name, health, attack_power)

    def attack(self, target):
        damage = self.attack_power
        target.health -= damage
        print(f"{self.name} bites {target.name} for {damage} damage!")
    
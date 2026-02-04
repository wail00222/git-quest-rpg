from .unit import Unit

class Warrior(Unit):
    def __init__(self, name):
        super().__init__(
            name=name,
            unit_type="warrior",
            damage_range=[3, 4, 5],
            luck=5,
            flee=3,
            price=10
        )
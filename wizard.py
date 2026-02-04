from unit import Unit
class Wizard(Unit):
    def __init__(self, name):
        super().__init__(
            name=name,
            unit_type="wizard",
            damage_range=range(2, 5),
            luck=20,
            flee=10,
            price=15
        )
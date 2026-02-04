from unit import Unit 
class Hunter(Unit):
    def __init__(self, name):
        super().__init__(
            name=name,
            unit_type="hunter",
            damage_range=range(1, 3), 
            luck=10,
            flee=20,
            price=25
        )
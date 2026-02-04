class Loses:
    def __init__(self, warriors=0, hunters=0, wizards=0):
        self.nb_warriors = warriors
        self.nb_hunters = hunters
        self.nb_wizards = wizards

    def total_lost(self):
        """Retourne le nombre total d'unités perdues."""
        return self.nb_warriors + self.nb_hunters + self.nb_wizards

    def __repr__(self):
        return (f"Pertes : {self.nb_warriors} Guerriers, "
                f"{self.nb_hunters} Chasseurs, "
                f"{self.nb_wizards} Magiciens")
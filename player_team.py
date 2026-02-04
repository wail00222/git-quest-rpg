from .team import Team

class PlayerTeam(Team):
    def __init__(self, members, warriors, hunters, wizards, damage, loot, flee):
        super().__init__(members)
        self.__nb_warriors = warriors
        self.__nb_hunters = hunters
        self.__nb_wizards = wizards
        self.__damage = damage
        self.__loot = loot
        self.__flee = flee

    def get_damage(self): return self.__damage
    def get_flee(self): return self.__flee
    def get_counts(self):
        return (self.__nb_warriors, self.__nb_hunters, self.__nb_wizards)

    def __repr__(self):
        return f"Team Player: {len(self._members)} units (W:{self.__nb_warriors}, H:{self.__nb_hunters}, M:{self.__nb_wizards})"
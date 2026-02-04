from abc import ABC, abstractmethod

class Team(ABC):
    def __init__(self, members=None):
        self._members = members if members else []

    def __len__(self):
        return len(self._members)

    def __getitem__(self, index):
        return self._members[index]
import random
from abc import ABC, abstractmethod


class Dice(ABC):
    @abstractmethod
    def throw_dice(self):
        pass


class NormalDice(Dice):
    def throw_dice(self):
        return random.randint(1, 6)


class CrookedDice(Dice):
    def throw_dice(self):
        return random.randrange(2, 16, 2)

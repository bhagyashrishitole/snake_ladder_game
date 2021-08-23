import unittest

from src.dice import NormalDice
from src.player import Player


class TestPlayer(unittest.TestCase):

    def setUp(self) -> None:
        self.__dice = NormalDice()
        self.__player = Player('Ram', self.__dice)

    def test_play_turn_return_int_value(self):
        next_position = self.__player.play_turn()
        self.assertIsInstance(next_position, int)


if __name__ == '__main__':
    unittest.main()

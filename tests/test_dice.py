import unittest

from src.dice import NormalDice, CrookedDice


class TestPlayer(unittest.TestCase):

    def setUp(self) -> None:
        self.__normal_dice = NormalDice()
        self.__crooked_dice = CrookedDice()

    def test_normal_dice_throw_return_between_1_to_6(self):
        for _ in range(10):
            next_position = self.__normal_dice.throw_dice()
            assert 1 <= next_position <= 6

    def test_crooked_dice_throw_return_even_no_between_2_to_16(self):
        for _ in range(10):
            next_position = self.__crooked_dice.throw_dice()
            assert next_position % 2 == 0
            assert 2 <= next_position <= 16


if __name__ == '__main__':
    unittest.main()

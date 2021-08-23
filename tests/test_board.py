import unittest

from src.board import Board
from src.dice import NormalDice
from src.exceptions import GameOverException
from src.player import Player
from  src.snake import Snake


class TestGameBoard(unittest.TestCase):

    def setUp(self) -> None:
        self.__dice = NormalDice()
        self.__player = Player('Alexa', self.__dice)
        self.__snakes = Snake(50, 20)
        self.__ladders = {2: 48}
        self.__board = Board(self.__ladders)
        self.__board.add_snakes([self.__snakes])

    def test_move_changes_player_position(self):
        previous_position = self.__player.position
        dice_value = self.__player.play_turn()
        self.__board.move(self.__player, dice_value)
        assert self.__player.position != previous_position

    def test_move_raise_game_over_exception(
            self):
        self.__player.position = 99
        dice_value = self.__player.play_turn()
        self.assertRaises(GameOverException,
                          lambda: self.__board.move(self.__player,
                                                    dice_value))

    def test_move_get_ladder(self):
        self.__player.position = 0
        dice_value = 2
        self.__board.ladders[2] = 48
        self.__board.move(self.__player, dice_value)
        assert self.__player.position == 48

    def test_move_snake_bite(self):
        self.__player.position = 47
        dice_value = 3
        self.__board.add_snakes([Snake(50, 2)])
        self.__board.move(self.__player, dice_value)
        print("---", self.__player.position)
        assert self.__player.position == 2


if __name__ == '__main__':
    unittest.main()

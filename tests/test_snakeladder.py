import unittest
from unittest.mock import MagicMock
from src.board import Board
from src.dice import NormalDice
from src.player import Player
from src.snake import Snake
from src.snakeladder import SnakeLadder


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.__dice = NormalDice()
        self.__players = [Player('Ram', self.__dice)]
        self.__snake1 = Snake(10, 4)
        self.__ladders = {}
        self.__board = Board(self.__ladders)
        self.__board.add_snakes([self.__snake1])
        self.__snake_ladder = SnakeLadder(self.__players, self.__board, 1)

    def test_play_calls_play_turn(self):
        for player in self.__players:
            player.play_turn = MagicMock(return_value=2)
        self.__snake_ladder.play()
        for player in self.__players:
            player.play_turn.assert_called_with()

    def test_play_GameOverException(self):
        self.__ladders[2] = 100
        for player in self.__players:
            player.play_turn = MagicMock(return_value=2)
        self.__snake_ladder.play()


if __name__ == '__main__':
    unittest.main()

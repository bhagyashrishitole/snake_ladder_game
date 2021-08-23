from src.board import Board
from src.dice import NormalDice
from src.player import Player
from src.snake import Snake
from src.snakeladder import SnakeLadder

if __name__ == '__main__':
    dice = NormalDice()
    players = [Player('Alexa', dice)]
    snake1 = Snake(head=15, tail=3)
    ladders = {4: 100, 25: 78}
    board = Board(ladders)
    board.add_snakes([snake1])
    game = SnakeLadder(players, board, 10)
    game.play()

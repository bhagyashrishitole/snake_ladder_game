import time

from src.exceptions import GameOverException


class Board:
    def __init__(self, ladders):
        self.snakes = dict()
        self.ladders = ladders
        self.start = 0
        self.end = 100

    def add_snakes(self, snakes):
        for each in snakes:
            self.snakes[each.head] = each

    def move(self, player, value_on_dice):
        next_value = player.position + value_on_dice
        if self.snakes.get(next_value):
            print(
                f'Snake bites to player {player.name} with start position {next_value} to '
                f'{self.snakes.get(next_value).tail}')
            time.sleep(2)
            player.position = self.snakes.get(next_value).tail
        elif self.ladders.get(next_value):
            print(f'{player.name} got ladder with start position {next_value} to {self.ladders.get(next_value)}')
            time.sleep(2)
            player.position = self.ladders.get(next_value)
        else:
            player.position = next_value
        if player.position >= self.end:
            print(f'Congratulations!! {player.name} won the game!')
            raise GameOverException

import time


class Player:
    def __init__(self, name, dice):
        self.name = name
        self.position = 0
        self.dice = dice

    def play_turn(self):
        print(f'Throwing dice for player: {self.name}')
        time.sleep(2)
        value_on_dice = self.dice.throw_dice()
        print(f'Got {value_on_dice}')
        return value_on_dice

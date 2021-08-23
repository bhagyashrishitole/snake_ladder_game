from src.exceptions import GameOverException


class SnakeLadder:
    def __init__(self, players, board, turns):
        self.players = players
        self.board = board
        self.turns = turns

    def play(self):
        current_turn = 0
        while True:
            for player in self.players:
                try:
                    value_on_dice = player.play_turn()
                    self.board.move(player, value_on_dice)
                    print(
                        f'Player {player.name} position: {player.position}')
                except GameOverException:
                    print(
                        f'Player {player.name} position: {player.position}')
                    return
            current_turn += 1
            if self.turns and current_turn >= self.turns:
                print(f'Game over!<(ツ)>!  All turns are over.')
                break

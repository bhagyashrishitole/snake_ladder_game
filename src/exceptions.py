class GameOverException(Exception):
    def __init__(self):
        self.msg = "Game over !!"

    def __str__(self):
        return repr(self.msg)

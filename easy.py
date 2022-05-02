import random


class Easy:
    def __init__(self, game):
        self.game = game

    def set_easy_move(self):
        """Randomly selects the computer's move."""
        move = f'{random.choice(["1", "2", "3"])} {random.choice(["1", "2", "3"])}'
        if self.game.computer_move_valid(move):
            self.game.current_move = [int(move[0]), int(move[-1])]
            return True
        else:
            return self.set_easy_move()

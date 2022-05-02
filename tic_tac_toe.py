import sys
from matrix import Matrix
from easy import Easy
from medium import Medium
from hard import Hard


class TicTacToe:
    def __init__(self):
        self.game_matrix = Matrix()
        self.start_commands = []
        self.player_1 = ''
        self.player_2 = ''
        self.current_move = [0, 0]
        self.current_character = 'X'
        self.next_character = 'O'
        self.turn = ''
        self.game_is_over = None

    def play_game(self):
        """The main call of the class."""
        self._set_starting_parameters()
        self._print_game_matrix()

        self._game_loop()
        return

    def _game_loop(self):
        """Playing the game."""
        player_1_move = getattr(self, 'set_' + self.player_1 + '_move')
        player_2_move = getattr(self, 'set_' + self.player_2 + '_move')

        while True:
            if self.turn != 'user':
                print(f'Making move level "{self.turn}"')

            if self.turn == self.player_1:
                player_1_move()
            elif self.turn == self.player_2:
                player_2_move()

            if not self._continue_game():
                return

    def _set_player_attributes(self):
        """Sets the player_1, player_2, and turn attributes"""
        self.player_1 = self.start_commands[1]
        self.player_2 = self.start_commands[2]
        self.turn = self.player_1
        return

    def _continue_game(self):
        """The repeated actions required after a move to prepare for the next move."""
        self._update_game_matrix()
        self._print_game_matrix()
        self._set_characters()
        self._print_game_state()

        if self.game_is_over:
            return False

        self._flip_turn()

        return True

    def _set_starting_parameters(self):
        """Sets the starting commands from the user."""
        commands = input("Input command: ").split()
        if self._commands_are_valid(commands):
            self._set_player_attributes()
            return
        else:
            print("Bad parameters!")
            return self._set_starting_parameters()

    def _commands_are_valid(self, commands):  # Method-helper
        """Sets the starting commands attribute if the commands are valid"""
        if commands[0] == 'exit':
            sys.exit()

        if len(commands) != 3:
            return False

        choices = ['user', 'easy', 'medium', 'hard']
        if all([commands[0] == 'start', commands[1] in choices, commands[2] in choices]):
            self.start_commands = commands
            return True

        return False

    def _print_game_matrix(self):
        m = self.game_matrix.matrix
        row_1 = f'| {m[0][0]} {m[0][1]} {m[0][2]} |'
        row_2 = f'| {m[1][0]} {m[1][1]} {m[1][2]} |'
        row_3 = f'| {m[2][0]} {m[2][1]} {m[2][2]} |'
        print('---------')
        print(row_1, row_2, row_3, sep='\n')
        print('---------')
        return

    def set_user_move(self):
        """Sets the move from the user."""
        move = input('Enter the coordinates: ')
        if self._user_move_valid(move):
            self.current_move = [int(move[0]), int(move[-1])]
            return

        return self.set_user_move()

    def set_easy_move(self):
        return Easy(self).set_easy_move()

    def set_medium_move(self):
        return Medium(self).set_medium_move()

    def set_hard_move(self):
        return Hard(self).set_hard_move()

    def computer_move_valid(self, move):  # Boolean, method-helper
        """Ensures that a valid move is given."""
        row = int(move[0])
        column = int(move[-1])

        if self.game_matrix.matrix[row - 1][column - 1] != ' ':
            return False

        return True

    def _user_move_valid(self, move):  # Boolean, method-helper
        """Ensures that a valid move is given."""
        try:
            row = int(move[0])
            column = int(move[-1])

            if self.game_matrix.matrix[row - 1][column - 1] != ' ':
                print("This cell is occupied! Choose another one!")
                return False

            if (not 1 <= row <= 3) or (not 1 <= column <= 3):
                print("Coordinates should be from 1 to 3!")
                return False

        except IndexError:
            print("Coordinates should be from 1 to 3!")
            return False

        except ValueError:
            print("You should enter numbers!")
            return False

        return True

    def _update_game_matrix(self):
        """Updates the game matrix with the current move."""
        move = self.current_move
        self.game_matrix.matrix[int(move[0]) - 1][int(move[-1]) - 1] = self.current_character
        return

    def _set_characters(self):
        """Sets the character attributes based on the turn that was just played."""
        if self.current_character == 'X':
            self.current_character = 'O'
            self.next_character = 'X'
        else:
            self.current_character = 'X'
            self.next_character = 'O'
        return

    def _print_game_state(self):
        """Updates the state of the game"""  # TODO split responsibilities here
        game_over_state = self._is_a_winner() or self._is_draw()
        self.game_is_over = game_over_state
        print(game_over_state or '')
        return

    def _is_a_winner(self):  # Method-helper
        """Determines if X or O has won the game."""
        threes = self.game_matrix.threes

        if ['X', 'X', 'X'] in threes:
            return 'X wins'
        if ['O', 'O', 'O'] in threes:
            return 'O wins'

        return False

    def _is_draw(self):  # Method-helper
        """Determines if the game is a draw."""
        if all([' ' not in row for row in self.game_matrix.rows]):
            return "It's a Draw!"

        return False

    def _flip_turn(self):
        """Switches turn between computer and user."""
        if self.turn == self.player_1:
            self.turn = self.player_2
            return
        if self.turn == self.player_2:
            self.turn = self.player_1
            return


game = TicTacToe()
game.play_game()

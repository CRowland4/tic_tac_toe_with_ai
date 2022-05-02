import copy
from matrix import Matrix


class Hard:
    def __init__(self, game):
        self.game = game
        self.original_board_list = []

    def set_hard_move(self):
        """Uses a minimax algorithm to play a move."""
        self._set_original_board_list()
        move = self._minimax(self.original_board_list, self.game.current_character)
        board_list_index = move['index']
        move_tuple = self._list_to_matrix_index(board_list_index)
        self.game.current_move = [move_tuple[0], move_tuple[1]]
        return

    def _list_to_matrix_index(self, index):  # Takes a number from 0-8, returns a 3x3 matrix location ('1 1' to '3 3')
        adjusted_index = index + 1
        row = (adjusted_index // 3.1)  # Yay math
        column = (adjusted_index + 2) % 3  # Yay math 2.0
        return int(row) + 1, column + 1

    def _set_original_board_list(self):
        """Sets the original_board_list attribute as a 9-element list of the current game board."""
        self.original_board_list = self._create_board_list(self.game.game_matrix)

    def _create_board_list(self, matrix_object):  # TODO rename this and the attribute after finishing
        """Returns a 9-element list from the given Matrix() object, with the spot index in place of empty spots."""
        matrix = copy.deepcopy(matrix_object.matrix)
        board_as_list = [*matrix[0], *matrix[1], *matrix[2]]

        for index, move in enumerate(board_as_list):
            if move == ' ':
                board_as_list[index] = index

        return board_as_list

    def _create_board_matrix(self, board_list):
        """Returns a Matrix() object from the given 9-element list."""
        function_board = Matrix()
        function_board.matrix[0] = [board_list[0], board_list[1], board_list[2]]
        function_board.matrix[1] = [board_list[3], board_list[4], board_list[5]]
        function_board.matrix[2] = [board_list[6], board_list[7], board_list[8]]

        return function_board

    def _give_empty_indices(self, board):
        """Returns a list of the empty indices from the given board."""
        return [element for element in board if type(element) == int]

    def _is_board_won(self, board, character):
        """Boolean, determines whether or not the given character has won the given board."""
        function_board = self._create_board_matrix(board)
        return True if [character, character, character] in function_board.threes else False

    def _minimax(self, new_board, character):
        """Returns the index of the best possible move for the given character."""
        available_spots = self._give_empty_indices(new_board)
        if self._is_board_won(new_board, self.game.current_character):
            return {'score': 10}
        if self._is_board_won(new_board, self.game.next_character):
            return {'score': -10}
        if len(available_spots) == 0:
            return {'score': 0}

        moves = []
        for spot in available_spots:
            move = {
                'index': spot,
                'score': 0  # This is a placeholder, so the structure of this dictionary is visible
            }

            new_board[spot] = character
            if character == self.game.current_character:
                result = self._minimax(new_board, self.game.next_character)
                move['score'] = result['score']
            elif character == self.game.next_character:
                result = self._minimax(new_board, self.game.current_character)
                move['score'] = result['score']

            new_board[spot] = move['index']
            moves.append(move)

        if character == self.game.current_character:
            best_score = -10000
            for index, move in enumerate(moves):
                if move['score'] > best_score:
                    best_score = move['score']
                    best_move = index
        elif character == self.game.next_character:
            best_score = 10000
            for index, move in enumerate(moves):
                if move['score'] < best_score:
                    best_score = move['score']
                    best_move = index

        return moves[best_move]

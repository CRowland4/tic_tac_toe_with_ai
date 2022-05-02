class Medium:
    def __init__(self, game):
        self.game = game

    def set_medium_move(self):
        if not self.try_medium_move():
            return self.game.set_easy_move()
        return

    def try_medium_move(self):
        """Makes a move that either wins, blocks a win, or returns False."""
        winning_move = self.find_winning_move(self.game.current_character)
        if winning_move:
            self.game.current_move = [winning_move[0], winning_move[1]]
            return True

        block_winning_move = self.find_winning_move(self.game.next_character)
        if block_winning_move:
            self.game.current_move = [block_winning_move[0], block_winning_move[1]]
            return True

        return False

    def find_winning_move(self, character):
        """Determines if there is a winning move or winning block to be made."""
        for index, row in enumerate(self.game.game_matrix.rows):  # TODO put this block in a row function
            if row.count(character) == 2 and ' ' in row:
                move = (index + 1, row.index(' ') + 1)
                return move

        # transposed_game_matrix = numpy.transpose(numpy.array(copy.deepcopy(self.game.game_matrix)))
        # transposed_game_matrix = transposed_game_matrix.tolist().matrix
        for index, column in enumerate(self.game.game_matrix.columns):  # TODO put this block in a column function
            if list(column).count(character) == 2 and ' ' in column:
                move = (list(column).index(' ') + 1, index + 1)
                return move

        main_diagonal = self.game.game_matrix.diagonals[0]
        if main_diagonal.count(character) == 2 and ' ' in main_diagonal:  # TODO put this block in a main diagonal func
            empty_spot = main_diagonal.index(' ') + 1
            move = (empty_spot, empty_spot)  # The row and column index are the same along the main diagonal.
            return move

        anti_diagonal = self.game.game_matrix.diagonals[1]
        if anti_diagonal.count(character) == 2 and ' ' in anti_diagonal:  # TODO put this block in an anti diagonal func
            if anti_diagonal.index(' ') == 0:
                move = (1, 3)
            if anti_diagonal.index(' ') == 1:  # TODO look at getting rid of these nested ifs using some _ % 3 algorithm
                move = (2, 2)
            if anti_diagonal.index(' ') == 2:
                move = (3, 1)

            return move

        return False


# TODO think about removing numpy and just creating my own transpose in this class

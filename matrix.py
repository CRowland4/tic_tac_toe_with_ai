class Matrix:
    def __init__(self):
        self.matrix = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' '],
        ]

    @property
    def rows(self):
        return self.matrix

    @property
    def columns(self):
        columns = [
            [self.matrix[0][0], self.matrix[1][0], self.matrix[2][0]],
            [self.matrix[0][1], self.matrix[1][1], self.matrix[2][1]],
            [self.matrix[0][2], self.matrix[1][2], self.matrix[2][2]],
        ]
        return columns

    @property
    def diagonals(self):
        diagonals = [
            [self.matrix[0][0], self.matrix[1][1], self.matrix[2][2]],
            [self.matrix[0][2], self.matrix[1][1], self.matrix[2][0]]
        ]
        return diagonals

    @property
    def threes(self):
        threes = self.rows + self.columns + self.diagonals
        return threes

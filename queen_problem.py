class queen_problem(object):
    def __init__(self):
        self.i = 0

    # Check the position is valid or conflicted from row
    def isValid(self, column_state, row_index):
        # check rows and columns
        if len(set(column_state[:row_index + 1])) != len(column_state[:row_index + 1]):
            #print(column_state, row_index)
            return False
        for i in range(row_index):
            # check diagonals
            if abs(column_state[i] - column_state[row_index]) == int(row_index - i):
                #print(column_state, row_index)
                return False
        return True

    # Print the feasible states
    def printChessboard(self, column_state, n):
        #print(column_state)
        for row in range(n):
            line = ""
            for column in range(n):
                if column_state[row] == column:
                    line += "Q\t"
                else:
                    line += ".\t"
            print(line, "\n")

    # If the solutions are found, then print them. Or the slover keeps computing.
    def problemSlover(self, column_state, row_index, n):
        #print(column_state)
        #print(row_index)
        if row_index == n:
            self.i += 1
            print('Answer', self.i, ': ')
            self.printChessboard(column_state, n)
            return
        else:
            for num_column in range(n):
                column_state[row_index] = num_column
                #print(column_state[row_index])
                if self.isValid(column_state, row_index):
                    self.problemSlover(column_state, row_index+1, n)

    def solveNQueens(self, n):
        # Ininalize state
        column_state = [-1]*n
        row_index = 0

        self.problemSlover(column_state, row_index, n)

if __name__ == '__main__':
    # Set up the number of queen and size
    number_of_queens = 8

    qp = queen_problem()
    qp.solveNQueens(number_of_queens)
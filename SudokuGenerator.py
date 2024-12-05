import math, random

'''
This class generates a Sudoku – the puzzle as well as the solution
'''
class SudokuGenerator:
    # Constructor for the SudokuGenerator class
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.board = [ # 2d array of ints
            [0 for col in range(self.row_length)]
            for row in range(self.row_length)
        ]
        self.box_length = int(math.sqrt(row_length))

    '''
    Returns a 2D python list of numbers, which represents the board
    '''
    def get_board(self):
        return self.board

    '''
    Displays the board to the console
    '''
    def print_board(self):
        for row in self.board:
            for cell in row:
                print(cell, end=" ")
            print()

    '''
    Returns a Boolean value.
    Determines if num is contained in the given row of the board.
    '''
    def valid_in_row(self,row,num):
        return num not in self.board[row]

    '''
    Returns a Boolean value.
    Determines if num is contained in the given column of the board.
    '''
    def valid_in_col(self,col,num):
        for row in range(self.row_length):
            if self.board[row][col] == num:
                return False
        return True

    '''
    Returns a Boolean value.
    Determines if num is contained in the 3x3 box from 
    (row_start, col_start) to (row_start+2, col_start+2).
    '''
    def valid_in_box(self, row_start, col_start, num):
        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start +3):
                if self.board[row][col] == num:
                    return False
        return True

    '''
    Returns if it is valid to enter num at (row, col) in the board.
    '''
    def is_valid(self, row, col, num):
        # Find the starting coords for the box that num is in
        box_row_start = (row // self.box_length) * self.box_length
        box_col_start = (col // self.box_length) * self.box_length

        # Check validity of num
        return (self.valid_in_row(row, num) and
                self.valid_in_col(col, num) and
                self.valid_in_box(box_row_start, box_col_start, num))

    '''
    Randomly fills in values in the 3x3 box from 
    (row_start, col_start) to (row_start+2, col_start+2).
    '''
    def fill_box(self, row_start, col_start):
        for i in range(self.box_length):
            for j in range(self.box_length):
                random_value = random.randint(1, 9)
                while not self.is_valid(row_start, col_start, random_value):
                    random_value = random.randint(1, 9)
                self.board[row_start + i][col_start + j] = random_value

    '''
	Fills the three boxes along the main diagonal of the board.
	This is the first major step in generating a Sudoku.
    '''
    def fill_diagonal(self):
        for i in range(0,self.row_length,3):
            self.fill_box(i,i)

    '''
    Fills the remaining squares in the board.
	It is the second major step in generating a Sudoku.
    '''
    def fill_remaining(self, row, col):
        if col >= self.row_length and row < self.row_length - 1:
            row += 1
            col = 0
        if row >= self.row_length and col >= self.row_length:
            return True
        if row < self.box_length:
            if col < self.box_length:
                col = self.box_length
        elif row < self.row_length - self.box_length:
            if col == int(row // self.box_length * self.box_length):
                col += self.box_length
        else:
            if col == self.row_length - self.box_length:
                row += 1
                col = 0
                if row >= self.row_length:
                    return True

        for num in range(1, self.row_length+ 1):
            if self.is_valid(row, col, num):
                self.board[row][col] = num
                if self.fill_remaining(row, col + 1):
                    return True
                self.board[row][col] = 0
        return False

    '''
    It constructs a solution by calling fill_diagonal and fill_remaining.
    '''
    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    '''
    This method removes the appropriate number of cells from the board.
    This method should be called after generating the Sudoku solution.
    '''
    def remove_cells(
            self):  # Ihfaz: creates a list to store the random board cells that this function is gonna remove then use those indexes on the board list to be removed (set to 0) for the sudoku game to run
        cells_to_remove = []

        while len(cells_to_remove) < self.removed_cells:
            row = random.randint(0, 8)
            col = random.randint(0, 8)

            if (row, col) not in cells_to_remove: # if the random index is not already there, add to list
                cells_to_remove.append((row, col))

        for row, col in cells_to_remove:  # the board indexes that match with the indexes in the list that removes cells
            self.board[row][col] = 0

'''
Given size and removed, this function generates and returns 
a size-by-size sudoku board. 
The board has cleared removed number of cells. 
This function should just call the constructor and appropriate methods from the SudokuGenerator class.
'''
def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board

'''
DELETE test_sudoku() BEFORE FINAL PUBLICATION !
uncomment to test
'''
# def test_sudoku():
#     sudoku1 = SudokuGenerator(9, 20)
#
#     sudoku1.fill_values()
#     print("Sudoku Board After Filling:")
#     sudoku1.print_board()
#
#     sudoku1.remove_cells()
#     print("\nSudoku Board After Removing Cells:")
#     sudoku1.print_board()
#
# if __name__ == "__main__":
#     test_sudoku()
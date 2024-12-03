import math, random
from board import *

# This class generates a Sudoku – the puzzle as well as the solution
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

    # Returns a 2D python list of numbers, which represents the board
    def get_board(self):
        return self.board

    # Displays the board to the console
    def print_board(self):
        for row in self.board:
            for cell in row:
                print(cell, end=" ")
            print()

    def valid_in_row(self,row,num):
        return num not in self.board[row]

    def valid_in_col(self,col,num):
        for row in range(self.row_length):
            if self.board[row][col] == num:
                return False
        return True
	    
    def valid_in_box(self, row_start, col_start, num):
        for row in range(row_start, row_start + 3):
            for col in range(col_start, col_start +3):
                if self.board[row][col] == num:
                    return False
        return True

    def is_valid(self, row, col, num):
        return self.valid_in_row(row, num) and self.valid_in_col(col, num) and self.valid_in_box(row, col, num)

    '''
    Fills the specified 3x3 box with values
    For each position, generates a random digit which has not yet been used in the box

	Parameters:
	row_start and col_start are the starting indices of the box to check
	i.e. the box is from (row_start, col_start) to (row_start+2, col_start+2)

	Return: None
    '''

    def fill_box(self, row_start, col_start):
        for i in range(self.box_length):
            for j in range(self.box_length):
                random_value = random.randint(1, 9)
                while not self.is_valid(row_start, col_start, random_value):
                    random_value = random.randint(1, 9)
                self.board[row_start + i][col_start + j] = random_value

    '''
    Fills the three boxes along the main diagonal of the board
    These are the boxes which start at (0,0), (3,3), and (6,6)

	Parameters: None
	Return: None
    '''

    def fill_diagonal(self):
        for i in range(0,self.row_length,3):
            self.fill_box(i,i)


    '''
    DO NOT CHANGE
    Provided for students
    Fills the remaining cells of the board
    Should be called after the diagonal boxes have been filled

	Parameters:
	row, col specify the coordinates of the first empty (0) cell

	Return:
	boolean (whether or not we could solve the board)
    '''

    def fill_remaining(self, row, col):
        if (col >= self.row_length and row < self.row_length - 1):
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
    DO NOT CHANGE
    Provided for students
    Constructs a solution by calling fill_diagonal and fill_remaining

	Parameters: None
	Return: None
    '''

    def fill_values(self):
        self.fill_diagonal()
        self.fill_remaining(0, self.box_length)

    '''
    Removes the appropriate number of cells from the board
    This is done by setting some values to 0
    Should be called after the entire solution has been constructed
    i.e. after fill_values has been called

    NOTE: Be careful not to 'remove' the same cell multiple times
    i.e. if a cell is already 0, it cannot be removed again

	Parameters: None
	Return: None
    '''

    def remove_cells(
            self):  # Ihfaz: creates a list to store the random board cells that this function is gonna remove then use those indexes on the board list to be removed (set to 0) for the sudoku game to run
        cells_to_remove = []

        if Board.difficulty.lower() == "easy":  # 30 cells empty or removed for easy
            for x in range(30 + 1):
                row = random.randint(0, 10)
                col = random.randint(0, 10)
                for cell_row, cell_col in cells_to_remove:
                    if cell_row == row and cell_col == col:  # if the random index is already there, a new one is generated
                        row = random.randint(0, 10)
                        col = random.randint(0, 10)
                    else:
                        cells_to_remove.append((row, col))

        elif Board.difficulty.lower() == "medium":  # 40 cells empty or removed for medium
            for x in range(40 + 1):
                row = random.randint(0, 10)
                col = random.randint(0, 10)
                for cell_row, cell_col in cells_to_remove:
                    if cell_row == row and cell_col == col:  # if the random index is already there, a new one is generated
                        row = random.randint(0, 10)
                        col = random.randint(0, 10)
                    else:
                        cells_to_remove.append((row, col))

        elif Board.difficulty.lower() == "hard":  # 50 cells empty or removed for hard
            for x in range(50 + 1):
                row = random.randint(0, 10)
                col = random.randint(0, 10)
                for cell_row, cell_col in cells_to_remove:
                    if cell_row == row and cell_col == col:  # if the random index is already there, a new one is generated
                        row = random.randint(0, 10)
                        col = random.randint(0, 10)
                    else:
                        cells_to_remove.append((row, col))

        for cell_coords in cells_to_remove:  # the board indexes that match with the indexes in the list that removes cells
            self.board[cell_coords] = 0

'''
DO NOT CHANGE
Provided for students
Given a number of rows and number of cells to remove, this function:
1. creates a SudokuGenerator
2. fills its values and saves this as the solved state
3. removes the appropriate number of cells
4. returns the representative 2D Python Lists of the board and solution

Parameters:
size is the number of rows/columns of the board (9 for this project)
removed is the number of cells to clear (set to 0)

Return: list[list] (a 2D Python list to represent the board)
'''


def generate_sudoku(size, removed):
    sudoku = SudokuGenerator(size, removed)
    sudoku.fill_values()
    board = sudoku.get_board()
    sudoku.remove_cells()
    board = sudoku.get_board()
    return board

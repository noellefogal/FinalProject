import pygame
from constants import *
from cell import Cell

# This class generates a Sudoku – the puzzle as well as the solution
class SudokuGenerator:
    # Constructor for the SudokuGenerator class
    def __init__(self, row_length, removed_cells):
        self.row_length = row_length
        self.removed_cells = removed_cells
        self.screen = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE))
        self.board = [ # 2d array of cell objects
            [Cell(0, row, col, self.screen) for col in range(self.row_length)]
            for row in range(self.row_length)
        ]

    # Returns a 2D python list of numbers, which represents the board
    def get_board(self):
        return self.board

    # Displays the board to the console
    def print_board(self):
        for row in self.board:
            for cell in row:
                print(cell.value, end=" ")
            print()
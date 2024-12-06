from cell import *
from SudokuGenerator import *
from constants import *
import pygame

class Board:
  def __init__(self, width, height, screen, difficulty):
    self.width = width
    self.height = height
    self.screen = screen
    self.difficulty = difficulty.upper()
    self.slctd_cell = None
    self.creating_board = True

    difficulty_map = {
      'EASY': 30,
      'MEDIUM': 40,
      'HARD': 50
    }
    removed_cells = difficulty_map.get(self.difficulty, 30)
    puzzle, solution = generate_sudoku(9, removed_cells)

    self.initial_board = puzzle
    self.solved_board = solution
    self.current_board = [
      [0 for _ in range(9)]
      for _ in range(9)
    ]

    self.cells = [
      [Cell(self.initial_board[row][col], row, col, screen) for col in range(9)]
      for row in range(9)
    ]

  def draw(self, screen):
    for i in range(10):
      if i%3 == 0:
        pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (BOARD_SIZE, i * CELL_SIZE), 5)
        pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, BOARD_SIZE), 5)
      pygame.draw.line(screen, BLACK, (0, i*CELL_SIZE), (BOARD_SIZE, i*CELL_SIZE), 1)
      pygame.draw.line(screen, BLACK, (i*CELL_SIZE, 0), (i*CELL_SIZE, BOARD_SIZE), 1)
    if self.creating_board:
      for row in self.cells:
        for cell in row:
          cell.draw()
    self.creating_board = False


  def select(self, row, col):
    if self.slctd_cell is not None:
      self.slctd_cell.selected = False
    self.slctd_cell = self.cells[row][col]
    self.slctd_cell.selected = True
    self.slctd_cell.draw()


  def click(self, row, col):
    if row < BOARD_SIZE and col<BOARD_SIZE:
      return row//CELL_SIZE, col//CELL_SIZE
    else:
      return None

#part 2
  def clear(self):
    if self.slctd_cell is not None and self.initial_board[self.slctd_cell.row][self.slctd_cell.col] == 0:
      self.slctd_cell.set_sketched_value(0)
      self.slctd_cell.draw()

      
  def sketch(self,value):
    if self.slctd_cell is not None:
      self.slctd_cell.set_sketched_value(value)
      self.slctd_cell.draw()
    
  def place_number(self,value):
    if self.slctd_cell is not None and self.initial_board[self.slctd_cell.row][self.slctd_cell.col] == 0:
      self.clear()
      self.slctd_cell.set_cell_value(value)
      self.slctd_cell.draw()
      self.slctd_cell.selected = False
      self.slctd_cell = None
    
  def reset_to_original(self):
    for row in range(len(self.cells)):
      for cell in range(len(self.cells[row])):
        self.cells[row][cell].set_cell_value(self.initial_board[row][cell])
        self.cells[row][cell].set_sketched_value(0)
#part 3
  def is_full(self): #checks if the board is full of values 1-9
    for row in self.current_board:
      for cell in row:
        if cell == 0:
          return False
    return True

  def update_board(self): #updates the 2D board array with the user-sketched in values of each cell
    for row in range(len(self.current_board)):
      for col in range(len(self.current_board[row])):
        self.current_board[row][col] = self.cells[row][col].value

  def find_empty(self):
    for row in range(len(self.current_board)):
      for cell in range(len(self.current_board[row])):
        if self.current_board[row][cell] == 0:
          x,y = row,cell
          return x,y

  def check_board(self):
    for row in range(len(self.current_board)):
      for col in range(len(self.current_board[row])):
        if self.current_board[row][col] != self.solved_board[row][col]:
          return False
    return True


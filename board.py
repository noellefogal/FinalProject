#part 1
from constants import *
import pygame

class Board:
  def __init__(self, width, height, screen, difficulty = "EASY"):
    self.width = width
    self.height = height
    self.screen = screen
    self.difficulty = difficulty

  def draw(self, screen):
    for i in range(10):
      if i%3 == 0:
        pygame.draw.line(screen, BLACK, (0, i * CELL_SIZE), (BOARD_SIZE, i * CELL_SIZE), 5)
        pygame.draw.line(screen, BLACK, (i * CELL_SIZE, 0), (i * CELL_SIZE, BOARD_SIZE), 5)
      pygame.draw.line(screen, BLACK, (0, i*CELL_SIZE), (BOARD_SIZE, i*CELL_SIZE), 1)
      pygame.draw.line(screen, BLACK, (i*CELL_SIZE, 0), (i*CELL_SIZE, BOARD_SIZE), 1)

  def select(self, row, col):
    self.slctd_cell = (row, col)
    return self.slctd_cell

  def click(self, row, col):
    if row < BOARD_SIZE and col<BOARD_SIZE:
      return (row//CELL_SIZE, col//CELL_SIZE)
    else:
      return None

#part 2
  def clear(self):
    if cell.is_mutable:
        cell.set_cell_value(0)
        cell.set_sketched_value(0)
    else:
      pass
      
  def sketch(self,value):
    self.sketched_value = value
    
  def place_number(self,value):
    self.value = value
    self.sketch = 0
    
  def reset_to_original(self):
    for row in self.board:
      for cell in row:
        if cell.is_mutable:
          cell.set_cell_value(0)
          cell.set_sketched_value(0)
#part 3
  def is_full(self): #checks if the board is full of values 1-9
    for row in self.board:
      for cell in row:
        if board[row][cell] == 0
          return False
    return True

  def update_board(self):
    pass

  def find_empty(self):
    for row in self.board:
      for cell in row:
        if board[row][cell] == 0
          x,y = row,cell
          return (x,y)

  def check_board(self):
    pass
  

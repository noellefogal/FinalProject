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
    for i in range(9):
      pygame.draw.line(screen, BLACK, (0, i*CELL_SIZE), (BOARD_SIZE, i*CELL_SIZE))




#part 2
  #def clear(self):
   # self.value = 0
  #  self.sketch = 0
 # def sketch(self,value):
   # self.sketched_value = value
 # def place_number(self,value):
  #  self.value = value
   # self.sketch = 0
  #def reset_to_original(self):
   # self.value = original_value
   # self.sketch = 0
  

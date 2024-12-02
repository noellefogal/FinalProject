#part 1
class Board:
  def __init__(self, width, height, screen, difficulty):
    self.width = width
    self.height = height
    self.screen = screen
    self.difficulty = difficulty

#part 2
  def clear(self):
    self.value = 0
    self.sketch = 0
  def sketch(self,value):
    self.sketched_value = value
  def place_number(self,value):
    self.value = value
    self.sketch = 0
  def reset_to_original(self):
    self.value = original_value
    self.sketch = 0
  

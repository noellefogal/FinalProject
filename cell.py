import pygame
from constants import *

# Represents a single cell in the Sudoku board
class Cell:
    # Constructor for the Cell class
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = 0
        self.selected = False

    # Sets the cell's value
    def set_cell_value(self, value):
        self.value = value

    # Sets the sketched value for the cell
    def set_sketched_value(self, value):
        self.sketched_value = value

    # Draws the cell on the screen
    def draw(self):
        # Calculates the position and size of the cell
        x = self.col * CELL_SIZE
        y = self.row * CELL_SIZE
        cell_rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)

        font = pygame.font.Font(None, FONT_SIZE)

        # Draw highlight if selected
        if self.selected:
            pygame.draw.rect(self.screen, RED, cell_rect, SLCTD_LINE_WIDTH)

        # Draw permanent value
        if self.value != 0:
            text_surf = font.render(str(self.value), True, BLACK) # Black text
            text_rect = text_surf.get_rect(center=cell_rect.center) # Center the text within cell
            self.screen.blit(text_surf, text_rect)

        # Draw sketched value
        elif self.sketched_value != 0:
            text_surf = font.render(str(self.sketched_value), True, GRAY) # Gray text
            text_rect = text_surf.get_rect(topleft=(cell_rect.x + 5, cell_rect.y + 5)) # Offset slightly from corner
            self.screen.blit(text_surf, text_rect)
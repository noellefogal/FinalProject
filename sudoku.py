from FinalProject.SudokuGenerator import SudokuGenerator
from board import *
from cell import *
from SudokuGenerator import *
from constants import *
import pygame, sys

def main():
        first_click = True
        puzzle_board, solution_board = generate_sudoku(9, HARD)
        screen = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE))
        screen.fill(WHITE)
        board = Board(BOARD_SIZE, BOARD_SIZE, screen)
        board.draw(screen)
        clock = pygame.time.Clock()
        running = True
        while running:
            pygame.display.flip()
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if not first_click:
                        pygame.draw.rect(board.screen, WHITE, pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE), SLCTD_LINE_WIDTH)
                    board.draw(screen)
                    x1,y1 = event.pos
                    x, y = board.click(x1,y1)
                    board.select(x,y)
                    board.slctd_cell.draw()
                    first_click = False
                elif event.type == pygame.KEYDOWN:
                    numbers = {pygame.K_1 : 1, pygame.K_2 : 2, pygame.K_3 : 3, pygame.K_4 : 4, pygame.K_5 : 5, pygame.K_6 : 6, pygame.K_7 : 7, pygame.K_8 : 8, pygame.K_9 : 9}
                    for item in numbers:
                        if event.key == item:
                            board.slctd_cell.set_sketched_value(0)
                            board.slctd_cell.draw()
                            board.slctd_cell.set_sketched_value(numbers[item])
                            board.slctd_cell.draw()
                    if event.key == pygame.K_RETURN:
                        board.slctd_cell.set_cell_value(board.slctd_cell.sketched_value)
                        board.slctd_cell.draw()
                        board.slctd_cell.set_sketched_value(0)
                        board.slctd_cell.draw()

if __name__ == "__main__":
    main()



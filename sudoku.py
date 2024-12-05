from FinalProject.SudokuGenerator import SudokuGenerator
from board import *
from cell import *
from SudokuGenerator import *
import pygame, sys

def main():

        board = generate_sudoku(9, HARD)
        screen = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE))
        screen.fill(WHITE)
        cells = [[Cell(0, row, col, screen) for col in range(9)] for row in range(9)]
        i = 0
        j = 0
        for list in cells:
            for item in list:
                item.set_cell_value(board[i][j])
                item.set_sketched_value(board[i][j])
                j+=1
            j = 0
            i+=1
        for list in cells:
            for item in list:
                item.draw()



        #cells[0][0].set_cell_value(9)
        #print(cells[0][0].value)


        clock = pygame.time.Clock()
        running = True
        while running:
            board = Board(BOARD_SIZE, BOARD_SIZE, screen)
            board.draw(screen)
            pygame.display.flip()
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    pass




if __name__ == "__main__":
    main()



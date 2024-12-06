from board import *
from constants import *
import pygame



def main():
        first_click = True
        screen = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE))
        screen.fill(WHITE)
        board = Board(BOARD_SIZE, BOARD_SIZE, screen, "HARD")
        board.draw(screen)
        clock = pygame.time.Clock()
        running = True
        x = 0
        y = 0

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
                    first_click = False
                elif event.type == pygame.KEYDOWN:
                    numbers = {pygame.K_1 : 1, pygame.K_2 : 2, pygame.K_3 : 3, pygame.K_4 : 4, pygame.K_5 : 5, pygame.K_6 : 6, pygame.K_7 : 7, pygame.K_8 : 8, pygame.K_9 : 9}
                    keys = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
                    if not first_click:
                        for item in keys:
                            if event.key == item:
                                try:
                                    ogx = x
                                    ogy = y
                                    if event.key == pygame.K_LEFT:
                                        assert(0 <= x-1 <=8)
                                        x-=1
                                    if event.key == pygame.K_RIGHT:
                                        assert(0 <= x + 1 <= 8)
                                        x+=1
                                    if event.key == pygame.K_UP:
                                        assert(0 <= y - 1 <= 8)
                                        y-=1
                                    if event.key == pygame.K_DOWN:
                                        assert(0 <= y + 1 <= 8)
                                        y+=1
                                    pygame.draw.rect(board.screen, WHITE,pygame.Rect(ogx * CELL_SIZE, ogy * CELL_SIZE, CELL_SIZE, CELL_SIZE),SLCTD_LINE_WIDTH)
                                    board.draw(screen)
                                    board.select(x,y)
                                except:
                                    pass
                    for item in numbers:
                        if event.key == item:
                            board.clear()
                            board.sketch(numbers[item])
                    if event.key == pygame.K_RETURN:
                        board.place_number(board.slctd_cell.sketched_value)
                        board.update_board()






if __name__ == "__main__":
    main()



from board import *

def main():
    try:
        pygame.init()
        screen = pygame.display.set_mode((BOARD_SIZE, BOARD_SIZE))
        screen.fill(WHITE)
        clock = pygame.time.Clock()
        running = True
        while running:
            board = Board(BOARD_SIZE, BOARD_SIZE, screen)
            board.draw(screen)
            pygame.display.flip()
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

    finally:
        pygame.quit()


if __name__ == "__main__":
    main()



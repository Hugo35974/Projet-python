import sys

from Couleurs import *
from Interface import newBoard

if __name__ == "__main__":
    pygame.init()
    Win = pygame.display.set_mode((Width, Height))
    pygame.display.set_caption("Chess Game")

    board = newBoard(Width, Height, Rows, Cols, Square, Win)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        board.draw_Board()
        board.draw_pieces()
        pygame.display.flip()
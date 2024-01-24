import sys
import pygame
from Boutons import *
from pygame.locals import MOUSEBUTTONDOWN, QUIT

from Couleurs import *
from Interface import newBoard


def initialize_game(width, height):
    pygame.init()
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Chess Game")
    return win

if __name__ == "__main__":
    # Taille initiale de la fenêtre
    initial_window_width, initial_window_height = 800, 600
    rows, cols = 8, 8
    square_size = initial_window_width // rows

    # Initialiser la fenêtre Pygame
    game_win = initialize_game(1250, 800)

    # Créer le plateau d'échecs
    chess_board = newBoard(game_win)

    # Initialiser un bouton

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if play_button_rect.collidepoint(mouse_pos):
                    print("Jouer")
                elif settings_button_rect.collidepoint(mouse_pos):
                    print("Paramètre")
                elif quit_button_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

        # Dessiner le plateau d'échecs
        chess_board.draw_Board()
        chess_board.draw_pieces()

        # Dessiner les boutons
        play_button_rect, settings_button_rect, quit_button_rect = draw_buttons(game_win)

        pygame.display.flip()
        pygame.display.update()

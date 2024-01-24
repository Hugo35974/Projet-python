import sys
import pygame
from pygame.locals import QUIT, MOUSEBUTTONDOWN
from Interface import newBoard
from Couleurs import *

def initialize_game(width, height):
    pygame.init()
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Chess Game")
    return win

def draw_buttons(win, show_P1vsP2_button, show_IA_button):
    font = pygame.font.Font(None, 36)

    # Bouton "Jouer"
    play_button_rect = pygame.Rect(50, 200, 200, 50)
    pygame.draw.rect(win, (0, 255, 0), play_button_rect)
    play_text = font.render("Jouer", True, (0, 0, 0))
    win.blit(play_text, (
    play_button_rect.centerx - play_text.get_width() // 2, play_button_rect.centery - play_text.get_height() // 2))

    # Bouton "Paramètre"
    settings_button_rect = pygame.Rect(50, 300, 200, 50)
    pygame.draw.rect(win, (255, 255, 0), settings_button_rect)
    settings_text = font.render("Paramètre", True, (0, 0, 0))
    win.blit(settings_text, (settings_button_rect.centerx - settings_text.get_width() // 2,
                             settings_button_rect.centery - settings_text.get_height() // 2))

    # Bouton "Quitter"
    quit_button_rect = pygame.Rect(50, 400, 200, 50)
    pygame.draw.rect(win, (255, 0, 0), quit_button_rect)
    quit_text = font.render("Quitter", True, (0, 0, 0))
    win.blit(quit_text, (
    quit_button_rect.centerx - quit_text.get_width() // 2, quit_button_rect.centery - quit_text.get_height() // 2))

    return play_button_rect, settings_button_rect, quit_button_rect

def draw_sub_button(win):
    # Sous-Boutons de "Jouer"
    P1vsP2_button_rect = pygame.Rect(50, 250, 200, 50)
    pygame.draw.rect(win, (0, 255, 0), P1vsP2_button_rect)
    play_text = font.render("Joueur vs Joueur", True, (0, 0, 0))
    win.blit(play_text, (
        P1vsP2_button_rect.centerx - play_text.get_width() // 2, P1vsP2_button_rect.centery - play_text.get_height() // 2))

    IA_button_rect = pygame.Rect(50, 250, 200, 50)
    pygame.draw.rect(win, (0, 255, 0), IA_button_rect)
    play_text = font.render("Joueur vs IA", True, (0, 0, 0))
    win.blit(play_text, (
        IA_button_rect.centerx - play_text.get_width() // 2, IA_button_rect.centery - play_text.get_height() // 2))


if __name__ == "__main__":
    # Taille initiale de la fenêtre
    initial_window_width, initial_window_height = 800, 600
    rows, cols = 8, 8
    square_size = initial_window_width // rows

    # Initialiser la fenêtre Pygame
    game_win = initialize_game(1250, 800)

    # Créer le plateau d'échecs
    chess_board = newBoard(initial_window_width, initial_window_height, rows, cols, square_size, game_win)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if play_button_rect.collidepoint(mouse_pos):
                    print("Jouer")
                    play_button_rect = False
                    settings_button_rect = False
                    quit_button_rect = False
                    show_P1vsP2_button = True
                    show_IA_button = True
                elif settings_button_rect.collidepoint(mouse_pos):
                    print("Paramètre")
                elif quit_button_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()

        # Dessiner le plateau d'échecs
        chess_board.draw_Board()

        # Dessiner les boutons
        play_button_rect, settings_button_rect, quit_button_rect = draw_buttons(game_win, False, False)

        pygame.display.flip()
        pygame.display.update()

import sys
import time
import pygame
from pygame.locals import MOUSEBUTTONDOWN, QUIT
from Boutons import *
from Couleurs import *
from GestionnaireEchec import *
from Interface import newBoard
from Moteur import IA


def label2(texte,game_win):
    
    font = pygame.font.Font(None, 26)
    game_win.fill(Black)
    rendered_text = font.render(texte, True, (255, 255, 255))
    game_win.blit(rendered_text, (20, 620))

def initialize_game(width, height):
    pygame.init()
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Chess Game")
    return win

if __name__ == "__main__":
    # Initialiser la fenêtre Pygame
    game_win = initialize_game(1250, 800)
# Initialisation du gestionnaire de jeu

    # Créer le plateau d'échecs
    chess_board = newBoard(game_win)  # Ajustez les paramètres en conséquence

    waiting_for_second_click = False
    selected_piece = None
    echec = False

    echec_manager = GestionnaireEchec(chess_board)
    ia = IA(echequier=chess_board, couleur='Noir')
    pygame.mixer.init()
    pygame.mixer.music.load("jeu_dechec.mp3")
    # Initialiser un bouton
    # Créer un bouton son
    main_button = True
    bouton_son = BoutonSon(game_win, "Son", (50, 100, 200, 50), None, None)
    # Réglage du volume (de 0.0 à 1.0)
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(loops=5)  # Jouez le son d'échec


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
                    print("Désactiver le Son")
                    bouton_son.gerer_son()
                    if not bouton_son.son_active:
                        pygame.mixer.music.stop()
                    else:
                        pygame.mixer.music.play(loops=5)
                    bouton_son.afficher(game_win, main_button)
                elif quit_button_rect.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()
                
                if (
                    chess_board.GameBoard <= mouse_pos[0] <= chess_board.GameBoard + chess_board.Cols * chess_board.Square and
                    0 <= mouse_pos[1] <= chess_board.Rows * chess_board.Square
                ):
                    col = (mouse_pos[0] - chess_board.GameBoard) // chess_board.Square
                    row = mouse_pos[1] // chess_board.Square
                    position = (row, col)

                    if not waiting_for_second_click:
                        try:
                            piece = chess_board.get_piece(position)
                            waiting_for_second_click = True
                        except:
                            texte ="Choisissez une pièce"
                    else:
                        print(piece)
                        if piece and piece.couleur == chess_board.current_player:
                            echec_resolu = echec_manager.est_mouvement_valide_resout_echec(piece, position)
                            print(echec_resolu)
                        else:
                            texte ="Sélectionnez une pièce valide."
                        waiting_for_second_click = False



        # Dessiner le plateau d'échecs
        chess_board.draw_Board()
        chess_board.draw_pieces()
        # Dessiner les boutons
        play_button_rect, settings_button_rect, quit_button_rect = draw_buttons(game_win)
        # Afficher le bouton son
        bouton_son.afficher(game_win, main_button)
        pygame.display.flip()
        pygame.display.update()

import sys

import pygame
from pygame.locals import MOUSEBUTTONDOWN, QUIT

from Boutons import *
from Couleurs import *
from GestionnaireEchec import *
from Interface import newBoard


def initialize_game(width, height):
    pygame.init()
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Chess Game")
    return win

if __name__ == "__main__":
    # Initialiser la fenêtre Pygame
    game_win = initialize_game(1250, 800)

    # Créer le plateau d'échecs
    chess_board = newBoard(game_win)  # Ajustez les paramètres en conséquence

    waiting_for_second_click = False
    selected_piece = None
    echec = False

    echec_manager = GestionnaireEchec(chess_board)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                if (
                    chess_board.GameBoard <= mouse_pos[0] <= chess_board.GameBoard + chess_board.Cols * chess_board.Square and
                    0 <= mouse_pos[1] <= chess_board.Rows * chess_board.Square
                ):
                    col = (mouse_pos[0] - chess_board.GameBoard) // chess_board.Square
                    row = mouse_pos[1] // chess_board.Square
                    position = (row, col)

                    if not waiting_for_second_click:
                        try :
                            piece = chess_board.get_piece(position)
                            waiting_for_second_click = True
                        except :
                            print("choisi une piece")
                    else:
                        print(piece)
                        if piece and piece.couleur == chess_board.current_player:
                            echec_resolu = echec_manager.est_mouvement_valide_resout_echec(piece, position)
                            print(echec_resolu)
                            waiting_for_second_click = False


                        else:
                            print("Sélectionnez une pièce valide.")
                            waiting_for_second_click = False




        # Dessiner le plateau d'échecs
        chess_board.draw_Board()
        chess_board.draw_pieces()
        draw_buttons(game_win)
        pygame.display.flip()
        pygame.display.update()

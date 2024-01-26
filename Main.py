import sys

import pygame
from pygame.locals import MOUSEBUTTONDOWN, QUIT

from Boutons import *
from Couleurs import *
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
    temp_board = newBoard(game_win)
    waiting_for_second_click = False
    selected_piece = None
    echec = False

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
                        piece = chess_board.get_piece(position)
                        if piece and piece.couleur == chess_board.current_player:
                            waiting_for_second_click = True
                            selected_piece = piece
                        else:
                            print("Sélectionnez une pièce valide.")
                    else:
                        if selected_piece and selected_piece.couleur == chess_board.current_player:
                            # Copiez la situation actuelle du plateau pour vérifier si le mouvement résout l'échec
                            temp_board = chess_board.clone_board()
                            adverse_color = 'Noir' if chess_board.current_player == 'Blanc' else 'Blanc'

                            # Vérifier si le mouvement est valide et résout l'échec
                            if temp_board.est_deplacement_valide(selected_piece, position):
                                temp_board.move(selected_piece, position)
                                
                                # Vérifier si le joueur actuel est en échec après le mouvement
                                if temp_board.est_echec(adverse_color):
                                    print(f"Le joueur {adverse_color} est en échec")
                                    

                                # Si le mouvement est valide et ne met pas le joueur actuel en échec, effectuez-le
                                

                                # Vérifier si le joueur actuel est en échec après le mouvement
                                if chess_board.est_echec(chess_board.current_player):
                                    if temp_board.est_echec(chess_board.current_player):
                                        print(f"Rejouer")
                                        temp_board.undo_last_move()
                                        waiting_for_second_click = False
                                        
                                    else:
                                        chess_board.move(selected_piece, position)
                                        chess_board.switch_player()
                                        waiting_for_second_click = False

                                else:
                                    chess_board.move(selected_piece, position)
                                    chess_board.switch_player()
                                    waiting_for_second_click = False
                            else:
                                print("Déplacement non valide. Rejouez.")
                                temp_board.undo_last_move()
                                waiting_for_second_click = False
                        else:
                            print("Sélectionnez une pièce valide.")
                            temp_board.undo_last_move()
                            waiting_for_second_click = False



        # Dessiner le plateau d'échecs
        chess_board.draw_Board()
        chess_board.draw_pieces()
        draw_buttons(game_win)
        pygame.display.flip()
        pygame.display.update()

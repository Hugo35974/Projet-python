import pygame

from Interface import *


def initialize_game(width, height):
    pygame.init()
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Chess Game")
    return win
    
game_win = initialize_game(1250, 800)

class GestionnaireEchec:
    def __init__(self, chess_board):
        self.chess_board = chess_board
        self.temp_board = chess_board

    def est_mouvement_valide_resout_echec(self, selected_piece, position):
        adverse_color = 'Noir' if self.chess_board.current_player == 'Blanc' else 'Blanc'

        if self.chess_board.est_deplacement_valide(selected_piece, position):
            self.temp_board.move(selected_piece, position)

            if self.temp_board.est_echec(adverse_color):
                print(f"Le joueur {adverse_color} est en échec")

            if self.chess_board.est_echec(self.chess_board.current_player):
                if self.temp_board.est_echec(self.chess_board.current_player):
                    self.temp_board.undo_last_move()
                    print("Rejoue")
                    return False
                else:
                    self.chess_board.move(selected_piece, position)
                    self.chess_board.switch_player()
                    return True
            else:
                self.chess_board.move(selected_piece, position)
                self.chess_board.switch_player()
                return True
        else:
            print("Déplacement non valide. Rejouez.")
            return False
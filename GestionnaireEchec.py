
from Interface import *
from Main import *

class GestionnaireEchec:
    def __init__(self, chess_board):
        self.chess_board = chess_board
        self.temp_board = chess_board

    def est_mouvement_valide_resout_echec(self, selected_piece, position):
        adverse_color = 'Noir' if self.chess_board.current_player == 'Blanc' else 'Blanc'
        if self.chess_board.est_deplacement_valide(selected_piece, position):
            self.temp_board.move(selected_piece, position)

            if self.temp_board.est_echec(adverse_color):
                texte = f"Le joueur {adverse_color} est en échec"
                label2(texte, self.temp_board.Win)
            else:
                texte = ""
                label2(texte, self.temp_board.Win)


            if self.chess_board.est_echec(self.chess_board.current_player):
                if self.temp_board.est_echec(self.chess_board.current_player):
                    self.temp_board.undo_last_move()
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


        

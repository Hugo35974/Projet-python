import time

import Main
from Interface import *
from Main import label2


class GestionnaireEchec:
    def __init__(self, chess_board):
        self.chess_board = chess_board
        self.temp_board = chess_board

    def est_mouvement_valide_resout_echec(self, selected_piece, position):
        adverse_color = 'Noir' if self.chess_board.current_player == 'Blanc' else 'Blanc'

        if self.chess_board.est_deplacement_valide(selected_piece, position):
            self.temp_board.move(selected_piece, position)

            # Vérifier l'échec adverse après le mouvement
            if self.temp_board.est_echec(adverse_color):
                texte = f"Le joueur {adverse_color} est en échec"
                label2(texte, self.temp_board.Win)

                # Vérifier l'échec et mat adverse
                if self.temp_board.est_en_echec_et_mat(adverse_color):
                    texte = f"Le joueur {adverse_color} est en échec et mat.\n Le joueur {self.chess_board.current_player} remporte la partie!"
                    texte_fin = f"Les {self.chess_board.current_player}s remportent la partie!"
                    pygame.draw.rect(self.temp_board.Win, (0, 0, 0), (20, 620, 500, 30))
                    font = pygame.font.SysFont('Arial', 22)
                    Main.blit_text(self.temp_board.Win, texte, (20, 620), font)
                    pygame.display.update()
                    # Peut-être ajouter ici une logique pour terminer la partie, redémarrer, etc.

            else:
                texte = ""
                label2(texte, self.temp_board.Win)

            # Annuler le mouvement s'il met le joueur en échec
            if self.temp_board.est_echec(self.chess_board.current_player):
                self.temp_board.undo_last_move()
                return False

            # Effectuer le mouvement et passer au joueur suivant
            self.chess_board.move(selected_piece, position)
            self.chess_board.switch_player()
            return True
        else:
            return False

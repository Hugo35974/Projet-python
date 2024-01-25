
class Joueur:
    def __init__(self):
        self.current_player = 'Blanc'  # Commencez avec les Blancs
        self.chess_board = ChessBoard()  # Assurez-vous d'adapter cela en fonction de votre implémentation

    def switch_player(self):
        if self.current_player == 'Blanc':
            self.current_player = 'Noir'
        else:
            self.current_player = 'Blanc'

    def play(self, position_from, position_to):
        piece = self.chess_board.get_piece(position_from)
        
        if piece and piece.couleur == self.current_player:
            if self.chess_board.est_deplacement_valide(piece, position_to):
                self.chess_board.move(piece, position_to)
                self.switch_player()
            else:
                print("Déplacement non valide pour la pièce sélectionnée.")
        else:
            print("Aucune pièce valide sélectionnée pour le joueur en cours.")

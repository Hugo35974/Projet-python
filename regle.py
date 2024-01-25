# class ReglesDuJeu:
#     def est_deplacement_valide(piece, dposition,grille):
#         """
#         Vérifie si un déplacement est valide selon les règles du jeu.

#         :param piece: Instance de la classe Piece.
#         :param depart: Tuple (ligne, colonne) représentant la position de départ.
#         :param arrivee: Tuple (ligne, colonne) représentant la position d'arrivée.
#         :param grille: Instance de la classe Grille représentant le plateau de jeu.
#         :return: True si le déplacement est valide, False sinon.
#         """
#         if piece and piece.deplacements_possibles(depart,grille):
#             return arrivee in piece.deplacements_possibles(depart,grille)
#         return False

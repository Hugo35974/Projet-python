class Piece:
    def __init__(self, couleur):
        self.couleur = couleur  # 'blanche' ou 'noire'

    def deplacements_possibles(self, position_actuelle, grille):
        """
        Méthode pour obtenir les déplacements possibles pour la pièce.
        :param position_actuelle: Tuple (ligne, colonne) représentant la position actuelle de la pièce sur la grille.
        :param grille: Instance de la classe Grille représentant le plateau de jeu.
        :return: Liste de tuples (ligne, colonne) représentant les positions où la pièce peut se déplacer.
        """
        raise NotImplementedError("Erreur de déplacement")

class Tour(Piece):
    def __init__(self, couleur):
        super().__init__(couleur)

    def deplacements_possibles(self, position_actuelle, grille):
        lignes, colonnes = grille.taille
        deplacements = []

        for i in range(lignes):
            if i != position_actuelle[0]:
                deplacements.append((i, position_actuelle[1]))

        for j in range(colonnes):
            if j != position_actuelle[1]:
                deplacements.append((position_actuelle[0], j))

        return deplacements


class Fou(Piece):
    def __init__(self, couleur):
        super().__init__(couleur)

    def deplacements_possibles(self, position_actuelle, grille):
        lignes, colonnes = grille.taille
        deplacements = []


        for i in range(1, min(lignes - position_actuelle[0], colonnes - position_actuelle[1])):
            deplacements.append((position_actuelle[0] + i, position_actuelle[1] + i))

        for i in range(1, min(position_actuelle[0] + 1, position_actuelle[1] + 1)):
            deplacements.append((position_actuelle[0] - i, position_actuelle[1] - i))

        for i in range(1, min(lignes - position_actuelle[0], position_actuelle[1] + 1)):
            deplacements.append((position_actuelle[0] + i, position_actuelle[1] - i))

        for i in range(1, min(position_actuelle[0] + 1, colonnes - position_actuelle[1])):
            deplacements.append((position_actuelle[0] - i, position_actuelle[1] + i))

        return deplacements

class Roi(Piece):
    def __init__(self, couleur):
        super().__init__(couleur)

    def deplacements_possibles(self, position_actuelle, grille):
        lignes, colonnes = grille.taille
        deplacements = []

        # Déplacements possibles (haut, bas, gauche, droite, diagonales)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]

        for direction in directions:
            nouvelle_ligne = position_actuelle[0] + direction[0]
            nouvelle_colonne = position_actuelle[1] + direction[1]

            if 0 <= nouvelle_ligne < lignes and 0 <= nouvelle_colonne < colonnes:
                deplacements.append((nouvelle_ligne, nouvelle_colonne))

        return deplacements


class Reine(Piece):
    def __init__(self, couleur):
        super().__init__(couleur)

    def deplacements_possibles(self, position_actuelle, grille):
        lignes, colonnes = grille.taille
        deplacements = []

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]

        for direction in directions:
            nouvelle_ligne, nouvelle_colonne = position_actuelle[0] + direction[0], position_actuelle[1] + direction[1]

            while 0 <= nouvelle_ligne < lignes and 0 <= nouvelle_colonne < colonnes:
                deplacements.append((nouvelle_ligne, nouvelle_colonne))
                if grille.case_est_vide((nouvelle_ligne, nouvelle_colonne)):
                    nouvelle_ligne += direction[0]
                    nouvelle_colonne += direction[1]
                else:
                    break

        return deplacements

class Cavalier(Piece):
    def __init__(self, couleur):
        super().__init__(couleur)

    def deplacements_possibles(self, position_actuelle, grille):
        lignes, colonnes = grille.taille
        deplacements = []

        mouvements = [
            (-2, -1), (-2, 1),
            (-1, -2), (-1, 2),
            (1, -2), (1, 2),
            (2, -1), (2, 1)
        ]

        for mouvement in mouvements:
            nouvelle_ligne = position_actuelle[0] + mouvement[0]
            nouvelle_colonne = position_actuelle[1] + mouvement[1]

            if 0 <= nouvelle_ligne < lignes and 0 <= nouvelle_colonne < colonnes:
                deplacements.append((nouvelle_ligne, nouvelle_colonne))

        return deplacements


class Pion(Piece):
    def __init__(self, couleur):
        super().__init__(couleur)

    def deplacements_possibles(self, position_actuelle, grille):
        lignes, colonnes = grille.taille
        deplacements = []

        direction = 1 if self.couleur == 'blanche' else -1


        nouvelle_ligne = position_actuelle[0] + direction
        nouvelle_colonne = position_actuelle[1]
        if 0 <= nouvelle_ligne < lignes and grille.case_est_vide((nouvelle_ligne, nouvelle_colonne)):
            deplacements.append((nouvelle_ligne, nouvelle_colonne))

            if (
                (self.couleur == 'blanche' and position_actuelle[0] == 1) or
                (self.couleur == 'noire' and position_actuelle[0] == lignes - 2)
            ):
                nouvelle_ligne = position_actuelle[0] + 2 * direction
                if grille.case_est_vide((nouvelle_ligne, nouvelle_colonne)):
                    deplacements.append((nouvelle_ligne, nouvelle_colonne))

        for delta_colonne in [-1, 1]:
            nouvelle_colonne = position_actuelle[1] + delta_colonne
            if 0 <= nouvelle_ligne < lignes and 0 <= nouvelle_colonne < colonnes and not grille.case_est_vide(
                (nouvelle_ligne, nouvelle_colonne)
            ) and grille.piece_a_couleur((nouvelle_ligne, nouvelle_colonne)) != self.couleur:
                deplacements.append((nouvelle_ligne, nouvelle_colonne))

        return deplacements
    

class PionBlanc(Pion):
    def __init__(self):
        super().__init__('blanche')

    def deplacements_possibles(self, position_actuelle, grille):
        lignes, colonnes = grille.taille
        deplacements = []

        direction = 1

        nouvelle_ligne = position_actuelle[0] + direction
        nouvelle_colonne = position_actuelle[1]
        if 0 <= nouvelle_ligne < lignes and grille.case_est_vide((nouvelle_ligne, nouvelle_colonne)):
            deplacements.append((nouvelle_ligne, nouvelle_colonne))

            if position_actuelle[0] == 1 and grille.case_est_vide((nouvelle_ligne + direction, nouvelle_colonne)):
                deplacements.append((nouvelle_ligne + direction, nouvelle_colonne))

        for delta_colonne in [-1, 1]:
            nouvelle_colonne = position_actuelle[1] + delta_colonne
            if 0 <= nouvelle_ligne < lignes and 0 <= nouvelle_colonne < colonnes and not grille.case_est_vide(
                (nouvelle_ligne, nouvelle_colonne)
            ) and grille.piece_a_couleur((nouvelle_ligne, nouvelle_colonne)) != self.couleur:
                deplacements.append((nouvelle_ligne, nouvelle_colonne))

        return deplacements


class PionNoir(Pion):
    def __init__(self):
        super().__init__('noire')

    def deplacements_possibles(self, position_actuelle, grille):
        lignes, colonnes = grille.taille
        deplacements = []

        direction = -1

        nouvelle_ligne = position_actuelle[0] + direction
        nouvelle_colonne = position_actuelle[1]
        if 0 <= nouvelle_ligne < lignes and grille.case_est_vide((nouvelle_ligne, nouvelle_colonne)):
            deplacements.append((nouvelle_ligne, nouvelle_colonne))

            if position_actuelle[0] == lignes - 2 and grille.case_est_vide((nouvelle_ligne + direction, nouvelle_colonne)):
                deplacements.append((nouvelle_ligne + direction, nouvelle_colonne))

        for delta_colonne in [-1, 1]:
            nouvelle_colonne = position_actuelle[1] + delta_colonne
            if 0 <= nouvelle_ligne < lignes and 0 <= nouvelle_colonne < colonnes and not grille.case_est_vide(
                (nouvelle_ligne, nouvelle_colonne)
            ) and grille.piece_a_couleur((nouvelle_ligne, nouvelle_colonne)) != self.couleur:
                deplacements.append((nouvelle_ligne, nouvelle_colonne))

        return deplacements


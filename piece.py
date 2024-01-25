import Couleurs


class Piece:
    def __init__(self, couleur,name):
        self.couleur = couleur
        self.name = name
        self.image = self.SVG()


    def deplacements_possibles(self, position_actuelle,Board):
        """
        Méthode pour obtenir les déplacements possibles pour la pièce.
        :param position_actuelle: Tuple (ligne, colonne) représentant la position actuelle de la pièce sur la 
        :param grille: Instance de la classe Grille représentant le plateau de jeu.
        :return: Liste de tuples (ligne, colonne) représentant les positions où la pièce peut se déplacer.
        """
        raise NotImplementedError("Erreur de déplacement")
    
    def SVG(self):
        pieces_dict = Couleurs.getImage()
        return pieces_dict[self.name]

class Tour(Piece):
    def __init__(self, couleur):
        self.name = "Tour"
        super().__init__(couleur, f"{self.name}_{couleur}")

    def deplacements_possibles(self, position_actuelle, grille):
        lignes, colonnes = grille.taille
        deplacements = []

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        for direction in directions:
            nouvelle_ligne, nouvelle_colonne = position_actuelle[0] + direction[0], position_actuelle[1] + direction[1]

            while 0 <= nouvelle_ligne < lignes and 0 <= nouvelle_colonne < colonnes:
                destination = (nouvelle_ligne, nouvelle_colonne)
                piece_destination = grille.get_piece(destination)

                if grille.case_est_vide(destination) or piece_destination.couleur != self.couleur:
                    deplacements.append(destination)

                    if not grille.case_est_vide(destination) and piece_destination.couleur != self.couleur:
                        # Si la case n'est pas vide et contient une pièce ennemie, on peut la prendre
                        break
                else:
                    # Si la case est occupée par une pièce alliée, on ne peut pas passer à travers
                    break

                nouvelle_ligne += direction[0]
                nouvelle_colonne += direction[1]

        return deplacements



class Fou(Piece):
    def __init__(self, couleur):
        self.name = "Fou"
        super().__init__(couleur, f"{self.name}_{couleur}")

    def deplacements_possibles(self, position_actuelle, grille):
        lignes, colonnes = grille.taille
        deplacements = []

        directions = [(1, 1), (-1, -1), (1, -1), (-1, 1)]

        for direction in directions:
            nouvelle_ligne, nouvelle_colonne = position_actuelle[0] + direction[0], position_actuelle[1] + direction[1]

            while 0 <= nouvelle_ligne < lignes and 0 <= nouvelle_colonne < colonnes:
                destination = (nouvelle_ligne, nouvelle_colonne)
                piece_destination = grille.get_piece(destination)

                if grille.case_est_vide(destination) or piece_destination.couleur != self.couleur:
                    deplacements.append(destination)

                    if not grille.case_est_vide(destination) and piece_destination.couleur != self.couleur:
                        # Si la case n'est pas vide et contient une pièce ennemie, on peut la prendre
                        break
                else:
                    # Si la case est occupée par une pièce alliée, on ne peut pas passer à travers
                    break

                nouvelle_ligne += direction[0]
                nouvelle_colonne += direction[1]

        return deplacements


class Roi(Piece):
    def __init__(self, couleur):
        self.name = "Roi"
        super().__init__(couleur, f"{self.name}_{couleur}")

    def deplacements_possibles(self, position_actuelle, grille):
        lignes, colonnes = grille.taille
        deplacements = []

        # Déplacements possibles (haut, bas, gauche, droite, diagonales)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]

        for direction in directions:
            nouvelle_ligne = position_actuelle[0] + direction[0]
            nouvelle_colonne = position_actuelle[1] + direction[1]

            if 0 <= nouvelle_ligne < lignes and 0 <= nouvelle_colonne < colonnes:
                destination = (nouvelle_ligne, nouvelle_colonne)
                piece_destination = grille.get_piece(destination)

                if grille.case_est_vide(destination) or piece_destination.couleur != self.couleur:
                    deplacements.append(destination)

        return deplacements



class Reine(Piece):
    def __init__(self, couleur):
        self.name = "Reine"
        super().__init__(couleur, f"{self.name}_{couleur}")

    def deplacements_possibles(self, coords_piece, grille):
        lignes, colonnes = grille.taille
        deplacements = []

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (-1, 1), (1, -1), (-1, -1)]

        for direction in directions:
            nouvelle_ligne, nouvelle_colonne = coords_piece[0] + direction[0], coords_piece[1] + direction[1]

            while 0 <= nouvelle_ligne < lignes and 0 <= nouvelle_colonne < colonnes:
                destination = (nouvelle_ligne, nouvelle_colonne)
                piece_destination = grille.get_piece(destination)

                if grille.case_est_vide(destination) or piece_destination.couleur != self.couleur:
                    deplacements.append(destination)

                    if not grille.case_est_vide(destination) and piece_destination.couleur != self.couleur:
                        # Si la case n'est pas vide et contient une pièce ennemie, on peut la prendre
                        break
                else:
                    # Si la case est occupée par une pièce alliée, on ne peut pas passer à travers
                    break

                nouvelle_ligne += direction[0]
                nouvelle_colonne += direction[1]

        return deplacements


class Cavalier(Piece):
    def __init__(self, couleur):
        self.name = "Cavalier"
        super().__init__(couleur, f"{self.name}_{couleur}")

    def deplacements_possibles(self, position_actuelle, grille):
        lignes, colonnes = 8,8
        deplacements = []

        mouvements = [
            (-2, -1), (-2, 1),
            (-1, -2), (-1, 2),
            (1, -2), (1, 2),
            (2, -1), (2, 1)
        ]

        piece_actuelle = grille.get_piece(position_actuelle)

        if piece_actuelle is None:
            return deplacements  # Aucun déplacement possible si la pièce actuelle est None

        for mouvement in mouvements:
            nouvelle_ligne = position_actuelle[0] + mouvement[0]
            nouvelle_colonne = position_actuelle[1] + mouvement[1]

            if 0 <= nouvelle_ligne < lignes and 0 <= nouvelle_colonne < colonnes:
                destination = (nouvelle_ligne, nouvelle_colonne)

                # Vérifier si la case de destination est vide ou occupée par une pièce ennemie
                if grille.case_est_vide(destination) or grille.piece_a_couleur(destination) != self.couleur:
                    deplacements.append(destination)

        return deplacements


class Pion(Piece):
    def __init__(self, couleur):
        self.name = "Pion"
        super().__init__(couleur, f"{self.name}_{couleur}")

    def deplacements_possibles(self, coords_piece, grille):
        lignes, colonnes = 8, 8
        deplacements = []

        direction = -1 if self.couleur == 'Blanc' else 1  # Inversion de la direction

        nouvelle_ligne = coords_piece[0] + direction
        nouvelle_colonne = coords_piece[1]
        if 0 <= nouvelle_ligne < lignes and grille.case_est_vide((nouvelle_ligne, nouvelle_colonne)):
            deplacements.append((nouvelle_ligne, nouvelle_colonne))

            if (
                (self.couleur == 'Blanc' and coords_piece[0] == lignes - 2) or
                (self.couleur == 'Noir' and coords_piece[0] == 1)
            ):
                nouvelle_ligne = coords_piece[0] + 2 * direction
                if grille.case_est_vide((nouvelle_ligne, nouvelle_colonne)):
                    deplacements.append((nouvelle_ligne, nouvelle_colonne))

        for delta_colonne in [-1, 1]:
            nouvelle_colonne = coords_piece[1] + delta_colonne
            if (
                0 <= nouvelle_ligne < lignes and
                0 <= nouvelle_colonne < colonnes and
                not grille.case_est_vide((nouvelle_ligne, nouvelle_colonne)) and
                grille.piece_a_couleur((nouvelle_ligne, nouvelle_colonne)) != self.couleur
            ):
                deplacements.append((nouvelle_ligne, nouvelle_colonne))

        return deplacements

import copy
import sys

import pygame

from Couleurs import *
from piece import *


class newBoard:
    def __init__(self, Win):
        self.Width = Couleurs.getWidth()
        self.Height = Couleurs.getHeight()
        self.Square = Couleurs.getSquare()
        self.GameBoard = self.Width // 2
        self.Win = Win
        self.Rows = Couleurs.getRows()
        self.Cols = Couleurs.getCols()
        self.Board = []
        self.selected = None
        self.create_Board()
        self.move_history = []
        self.taille = Couleurs.getRows(), Couleurs.getCols()
        self.current_player = 'Blanc'
        # Créer une surface distincte pour le plateau d'échecs
        self.board_surface = pygame.Surface((self.Square * self.Cols, self.Square * self.Rows))

    def switch_player(self):
        if self.current_player == 'Blanc':
            self.current_player = 'Noir'
        else:
            self.current_player = 'Blanc'


    def create_Board(self):
        for row in range(self.Rows):
            self.Board.append([None for _ in range(self.Cols)])

            for col in range(self.Cols):
                if row == 1:
                    self.Board[row][col] = Pion(Noir, col)
                elif row == 6:
                    self.Board[row][col] = Pion(Blanc, col)
                elif row == 0:
                    self.Board[row][col] = self.create_piece_for_row(Noir, row, col)
                elif row == 7:
                    self.Board[row][col] = self.create_piece_for_row(Blanc, row, col)

    def create_piece_for_row(self, couleur, row, col):
        if col == 0 or col == 7:
            return Tour(couleur,col)
        elif col == 1 or col == 6:
            return Cavalier(couleur,col)
        elif col == 2 or col == 5:
            return Fou(couleur,col)
        elif col == 3:
            return Reine(couleur,col)
        elif col == 4:
            return Roi(couleur,col)
        else:
            return None
        
    def get_valid_moves(self, piece):
        """
        Renvoie tous les mouvements valides pour une pièce donnée.
        """
        valid_moves = []
        for row in range(self.Rows):
            for col in range(self.Cols):
                target_position = (row, col)
                if self.est_deplacement_valide(piece, target_position):
                    valid_moves.append(target_position)
        return valid_moves
    
    def get_piece(self, position):
        if position:
            if 0 <= position[0] < self.Rows and 0 <= position[1] < self.Cols:
                return self.Board[position[0]][position[1]]
            else:
                return None
        else :return None

    def est_deplacement_valide(self, piece, position):

        if piece and position in piece.deplacements_possibles(self.coordonnees_piece(piece), self):
            return True
        else:
            return False

    def afficher_surbrillance(self, case, couleur):
        # Cette fonction change la couleur de fond de la case spécifiée
        ligne, colonne = case
        pygame.draw.rect(self.board_surface, couleur, (self.Square * colonne, self.Square * ligne, self.Square, self.Square))
        self.Win.blit(self.board_surface, (self.GameBoard, 0))
        
    def case_est_vide(self, position):
        if 0 <= position[0] < self.Rows and 0 <= position[1] < self.Cols:
            return self.Board[position[0]][position[1]] is None
        else:
            return False

        
    def coordonnees_piece(self, piece):
            
            for i in range(self.Rows):
                for j in range(self.Cols):
                    if self.get_piece((i, j))!= None :
                        if self.get_piece((i, j)) == piece:
                            return (i, j)
            return None
    
    def est_echec(self, couleur):
        roi_position = self.trouver_position_roi(couleur)
        
        # Vérifier si les pièces adverses menacent la position du roi
        for row in range(self.Rows):
            for col in range(self.Cols):
                piece = self.get_piece((row, col))
                if piece and piece.couleur != couleur:
                    deplacements_possibles = piece.deplacements_possibles((row, col), self)
                    if roi_position in deplacements_possibles:
                        return True

        return False
    
    def trouver_position_roi(self, couleur):
        for row in range(self.Rows):
            for col in range(self.Cols):
                piece = self.get_piece((row, col))
                if isinstance(piece, Roi) and piece.couleur == couleur:
                    return (row, col)
        return None
    
    def undo_last_move(self):
        if self.move_history:
            # Récupérer le dernier mouvement
            last_move = self.move_history.pop()
            # Inverser le dernier mouvement
            piece, from_coords, to_coords = last_move
            self.Board[from_coords[0]][from_coords[1]] = piece
            self.Board[to_coords[0]][to_coords[1]] = None

            # Mettez à jour d'autres éléments si nécessaire
            
    def piece_a_couleur(self, position):
        if 0 <= position[0] < self.Rows and 0 <= position[1] < self.Cols:
            piece = self.Board[position[0]][position[1]]
            if piece:
                return piece.couleur
            else:
                return None
        else:
            return None

    def est_en_echec_et_mat(self, couleur):
        roi_position = self.trouver_position_roi(couleur)

        # Vérifier si le roi est en échec
        if not self.est_echec(couleur):
            return False

        # Vérifier si le roi peut échapper à l'échec en effectuant un déplacement
        for i in range(self.Rows):
            for j in range(self.Cols):
                destination = (i, j)
                if self.est_deplacement_valide(self.get_piece(roi_position), destination):
                    # Si le roi peut effectuer un déplacement valide, ce n'est pas un échec et mat
                    return False

        # Vérifier si une autre pièce peut bloquer l'attaque
        for i in range(self.Rows):
            for j in range(self.Cols):
                piece = self.get_piece((i, j))
                if piece and piece.couleur == couleur:
                    deplacements_possibles = piece.deplacements_possibles((i, j), self)
                    for destination in deplacements_possibles:
                        # Vérifier si la pièce peut bloquer l'attaque en se déplaçant
                        if self.est_deplacement_valide(piece, destination):
                            return False

        # Si aucune condition n'est remplie, c'est un échec et mat
        return True



    def move(self, piece, position):
        # Obtenez les coordonnées de la pièce avant le déplacement
        coords_avant = self.coordonnees_piece(piece)
        
        if coords_avant is not None:
            # Mettez à jour la case d'origine en la rendant vide
            self.Board[coords_avant[0]][coords_avant[1]] = None
            self.move_history.append((piece, coords_avant, position))
            # Placez la pièce à sa nouvelle position
            self.Board[position[0]][position[1]] = piece

    def mouvement(self,coords_avant,position):
        
        if coords_avant is not None:
            # Mettez à jour la case d'origine en la rendant vide
            self.Board[coords_avant[0]][coords_avant[1]] = None
            self.move_history.append((self.get_piece(coords_avant), coords_avant, position))
            # Placez la pièce à sa nouvelle position
            self.Board[position[0]][position[1]] = self.get_piece(coords_avant)

    def draw_Board(self):
        # Dessiner le plateau d'échecs sur la surface distincte
        self.board_surface.fill(brown)
        for row in range(self.Rows):
            for col in range(row % 2, self.Cols, 2):
                pygame.draw.rect(self.board_surface, White, (self.Square * col, self.Square * row, self.Square, self.Square))
        # Afficher la surface du plateau d'échecs sur la fenêtre principale
        self.Win.blit(self.board_surface, (self.GameBoard, 0))

    def draw_pieces(self):
        for row in range(self.Rows):
            for col in range(self.Cols):
                piece = self.get_piece((row, col))
                if piece is not None:
                    piece_x = col * self.Square + self.GameBoard
                    piece_y = row * self.Square
                    self.Win.blit(piece.image, (piece_x, piece_y))

    def copy(self):
        #Création d'une copie de l'échequier
        copied_board = newBoard(self.Win)
        copied_board.Width = self.Width
        copied_board.Height = self.Height
        copied_board.Square = self.Square
        copied_board.GameBoard = self.GameBoard
        copied_board.Rows = self.Rows
        copied_board.Cols = self.Cols
        copied_board.current_player = self.current_player

        # Copy the actual board state
        copied_board.Board = [row[:] for row in self.Board]

        return copied_board

    def deplacerPieceEnIndex(self, indexDepart, indexArrivee):
        """
        Move a piece from the starting index to the destination index.
        """
        piece = self.get_piece(indexDepart)

        if piece is not None:
            self.Board[indexDepart[0]][indexDepart[1]] = None  # Empty the starting position
            self.Board[indexArrivee[0]][indexArrivee[1]] = piece  # Place the piece in the destination position
        else:
            print("No piece found at the starting position.")

    def coefficientPointsSiPeutEtreMangee(self, position):
        if 0 <= position[0] < self.Rows and 0 <= position[1] < self.Cols:
            piece = self.Board[position[0]][position[1]]
            if piece:
                # Ajoutez ici votre logique pour déterminer le coefficient de points
                # en fonction de si la pièce à la position spécifiée peut être mangée.
                # Vous pouvez retourner la valeur appropriée en fonction de votre logique.
                return 2  # Exemple : si la pièce peut être mangée, retourne 1
        return 1  # Par défaut, retourne 0 si la position est hors limites ou si la case est vide
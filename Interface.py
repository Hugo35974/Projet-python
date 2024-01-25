import sys

import pygame

from Couleurs import *
from piece import *
from regle import *


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
        self.taille = Couleurs.getRows(),Couleurs.getCols()
        self.current_player = 'Blanc'
        # Créer une surface distincte pour le plateau d'échecs
        self.board_surface = pygame.Surface((self.Square * self.Cols, self.Square * self.Rows))


    def switch_player(self):
        if self.current_player == 'Blanc':
            self.current_player = 'Noir'
        else:
            self.current_player = 'Blanc'

    def play(self, position_from, position_to):
        piece = self.Board.get_piece(position_from)
        
        if piece and piece.couleur == self.current_player:
            if self.Board.est_deplacement_valide(piece, position_to):
                self.Board.move(piece, position_to)
                self.switch_player()
            else:
                print("Déplacement non valide pour la pièce sélectionnée.")
        else:
            print("Aucune pièce valide sélectionnée pour le joueur en cours.")
            

    def create_Board(self):
        for row in range(self.Rows):
            self.Board.append([None for _ in range(self.Cols)])

            for col in range(self.Cols):
                if row == 1:
                    self.Board[row][col] = Pion(Noir)
                elif row == 6:
                    self.Board[row][col] = Pion(Blanc)
                elif row == 0:
                    self.Board[row][col] = self.create_piece_for_row(Noir, row, col)
                elif row == 7:
                    self.Board[row][col] = self.create_piece_for_row(Blanc, row, col)

    def create_piece_for_row(self, couleur, row, col):
        if col == 0 or col == 7:
            return Tour(couleur)
        elif col == 1 or col == 6:
            return Cavalier(couleur)
        elif col == 2 or col == 5:
            return Fou(couleur)
        elif col == 3:
            return Reine(couleur)
        elif col == 4:
            return Roi(couleur)
        else:
            return None

    def get_piece(self, position):
        if 0 <= position[0] < self.Rows and 0 <= position[1] < self.Cols:
            return self.Board[position[0]][position[1]]
        else:
            return None

    def est_deplacement_valide(self, piece, position):
        print(position)
        print(piece.deplacements_possibles(self.coordonnees_piece(piece), self))
        if piece and position in piece.deplacements_possibles(self.coordonnees_piece(piece), self):
            print("Déplacement possible")
            return True
        else:
            print("Déplacement non valide")
            return False
        
    def case_est_vide(self, position):
        if 0 <= position[0] < self.Rows and 0 <= position[1] < self.Cols:
            return self.Board[position[0]][position[1]] is None
        else:
            return False

    def piece_a_couleur(self, position):
        if 0 <= position[0] < self.Rows and 0 <= position[1] < self.Cols:
            piece = self.Board[position[0]][position[1]]
            if piece:
                return piece.couleur
            else:
                return None
        else:
            return None
        
    def coordonnees_piece(self, piece):
            
            for i in range(self.Rows):
                for j in range(self.Cols):
                    if self.get_piece((i, j)) == piece:
                        return (i, j)
            return None
    

    def move(self, piece, position):
        # Obtenez les coordonnées de la pièce avant le déplacement
        coords_avant = self.coordonnees_piece(piece)

        if coords_avant is not None:
            # Mettez à jour la case d'origine en la rendant vide
            self.Board[coords_avant[0]][coords_avant[1]] = None

            # Placez la pièce à sa nouvelle position
            self.Board[position[0]][position[1]] = piece
        else:
            print("La pièce n'a pas été trouvée sur le plateau.")


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


import sys

import pygame

import regle
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
        self.create_Board()


        # Créer une surface distincte pour le plateau d'échecs
        self.board_surface = pygame.Surface((self.Square * self.Cols, self.Square * self.Rows))

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

    def get_piece(self, row, col):
        return self.Board[row][col]

    # def move(self, piece, row, col):
    #     self.Board[piece.row][piece.col], self.Board[row][col] = self.Board[row][col], self.Board[piece.row][piece.col]
    #     piece.piece_move(row, col)

    #     if isinstance(piece, Pion):
    #         if piece.first_move:
    #             piece.first_move = False

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
                piece = self.get_piece(row, col)
                if piece is not None:
                    piece_x = col * self.Square + self.GameBoard
                    piece_y = row * self.Square
                    self.Win.blit(piece.image, (piece_x, piece_y))

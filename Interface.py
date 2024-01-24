import sys

import pygame
from piece import *
from Couleurs import *

class newBoard:
    def __init__(self, Width, Height, Rows, Cols, Square, Win):
        self.Width = Width
        self.Height = Height
        self.Square = Square
        self.GameBoard = self.Width // 2
        self.Win = Win
        self.Rows = Rows
        self.Cols = Cols
        self.Board = []
        self.create_Board()

        # Créer une surface distincte pour le plateau d'échecs
        self.board_surface = pygame.Surface((Square * Cols, Square * Rows))

    def create_Board(self):
        for row in range(self.Rows):
            self.Board.append([None for _ in range(self.Cols)])

            for col in range(self.Cols):
                if row == 1:
                    self.Board[row][col] = PionNoir()
                elif row == 6:
                    self.Board[row][col] = PionBlanc()
                elif row == 0:
                    self.Board[row][col] = self.create_piece_for_row(Black, row, col)
                elif row == 7:
                    self.Board[row][col] = self.create_piece_for_row(White, row, col)

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

    def move(self, piece, row, col):
        self.Board[piece.row][piece.col], self.Board[row][col] = self.Board[row][col], self.Board[piece.row][piece.col]
        piece.piece_move(row, col)

        if isinstance(piece, Pion):
            if piece.first_move:
                piece.first_move = False

    def draw_Board(self):
        # Dessiner le plateau d'échecs sur la surface distincte
        self.board_surface.fill(brown)
        for row in range(self.Rows):
            for col in range(row % 2, self.Cols, 2):
                pygame.draw.rect(self.board_surface, White, (self.Square * col, self.Square * row, self.Square, self.Square))

        # Afficher la surface du plateau d'échecs sur la fenêtre principale
        self.Win.blit(self.board_surface, (self.GameBoard, 0))

    def draw_piece(self, piece, Win):
        if piece is not None:
            Win.blit(piece.image, (piece.x + self.GameBoard, piece.y))

import os

import pygame

#Taille
Width, Height = 760, 760
Rows, Cols = 8, 8
Square = Width//Rows

#Couleurs
Bg = (47, 79, 79)
Black = (0, 0, 0)
White = (255, 255, 255)
beige = (245, 245, 220)
brown_chocolate = (210, 105, 30)
brown = (87, 16, 16)
cornsilk = (255, 248, 220)
Green = (0, 255, 0)

pieces_dict = {}
path = "./chess_images"

for piece in os.listdir(path):
    if piece.endswith(".png"):
        nomPiece = os.path.splitext(piece)[0]
        file_path = os.path.join("./chess_images", piece)
        image = pygame.transform.scale(pygame.image.load(file_path), (Square, Square))
        pieces_dict[nomPiece] = image

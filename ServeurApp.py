import ast
import sys
import threading
import time

import pygame
from pygame.locals import MOUSEBUTTONDOWN, QUIT

from Boutons import *
from Couleurs import *
from GestionnaireEchec import *
from Interface import newBoard
from Multiplayer import server


def initialize_game(width, height):
    pygame.init()
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Chess Game")
    return win

def label2(texte,game_win):
    
    font = pygame.font.Font(None, 26)
    game_win.fill(Black)
    rendered_text = font.render(texte, True, (255, 255, 255))
    game_win.blit(rendered_text, (20, 620))


def main():
    # Read the server IP from the file
    server_ip = open("Multiplayer/Master_ip.txt", "r").read().strip()
    nbPlayer = 2
    # Create a ChatServer instance and connect to the server
    chat_server = server.ChatServer(server_ip, 8080)
    chat_server_thread = threading.Thread(target=chat_server.start_server)
    chat_server_thread.start()
    tableau = []
    try:
        while True:
            # on va actualiser l'etat du jeu toute les 0.4 secondes, pour eviter que les messages ne se melangent
            time.sleep(0.4)
            if len(chat_server.GetClients()) == 1:

                try :
                    chat_server.broadcast((chat_server.GetReceivedMessages()).encode('utf-8'))

                except :
                    chat_server.EmptyMessages(nbPlayer)






    except KeyboardInterrupt:
        chat_server.close()
        print("Server closed")


if __name__ == "__main__":
    main()
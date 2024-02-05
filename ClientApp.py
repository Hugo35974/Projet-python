'''this is the main file for the client side of the game, c'est celle qui va uniquement lancer l'interface graphique
et ensuite envoyer les messages de l'état de son jeu au serveur
Exemple : le joueur 1 (client 1) a validé la carte 12, il va donc envoyer au serveur :

'''
import ast
import time

import pygame
from pygame.locals import MOUSEBUTTONDOWN, QUIT

from Boutons import *
from GestionnaireEchec import GestionnaireEchec
from Interface import *
from Multiplayer import client


def initialize_game(width, height):
    pygame.init()
    win = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Chess Game")
    return win

def main():
    # Read the server IP from the file
    game_win = initialize_game(1250, 800)
    server_ip = open("Multiplayer/Master_ip.txt", "r").read().strip()
    # Create a ChatClient instance and connect to the server
    clientChat = client.ChatClient(server_ip, 8080)
    clientChat.connect()
    time.sleep(0.1)# on attends une réponse du serveur
    chess_board = newBoard(game_win)
    # on fait une boucle infini pour pouvoir utiliser les threads.
    chec_manager = GestionnaireEchec(chess_board)
    pygame.mixer.init()
    pygame.mixer.music.load("jeu_dechec.mp3")
    # Initialiser un bouton
    # Créer un bouton son
    main_button = True
    bouton_son = BoutonSon(game_win, "Son", (50, 100, 200, 50), None, None)
    # Réglage du volume (de 0.0 à 1.0)
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.play(loops=5)  # Jouez le son d'échec
    echec_manager = GestionnaireEchec(chess_board)

    waiting_for_second_click = False
    selected_piece = None
    echec = False

    try:
        while True:
            msg = clientChat.GetReceivedMessages()
            try:
                string_data = msg[-1].replace(')(', '),(')
                tuple_data = ast.literal_eval(string_data)
                coords_avant, position = tuple_data
            except :
                coords_avant = None
                position = None
            if coords_avant and position:
                echec_manager.est_mouvement_valide_resout_echec(chess_board.get_piece(coords_avant), position)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    
                    if play_button_rect.collidepoint(mouse_pos):
                        print("Jouer")
                    elif settings_button_rect.collidepoint(mouse_pos):
                        print("Désactiver le Son")
                        bouton_son.gerer_son()
                        if not bouton_son.son_active:
                            pygame.mixer.music.stop()
                        else:
                            pygame.mixer.music.play(loops=5)
                        bouton_son.afficher(game_win, main_button)
                    elif quit_button_rect.collidepoint(mouse_pos):
                        pygame.quit()
                        sys.exit()
                    
                    if (
                        chess_board.GameBoard <= mouse_pos[0] <= chess_board.GameBoard + chess_board.Cols * chess_board.Square and
                        0 <= mouse_pos[1] <= chess_board.Rows * chess_board.Square
                    ):
                        col = (mouse_pos[0] - chess_board.GameBoard) // chess_board.Square
                        row = mouse_pos[1] // chess_board.Square
                        position = (row, col)
                        if not waiting_for_second_click:
                            try:
                                piece = chess_board.get_piece(position)
                                positionpiece = position
                                waiting_for_second_click = True
                                # Vérifiez si la pièce est une instance de la classe Pion
                                if isinstance(piece, Pion):
                                    deplacements_possibles = piece.deplacements_possibles(position, chess_board)
                                    print("Surbrillance positions:", deplacements_possibles)
                                    for d in deplacements_possibles:
                                        ligne, colonne = d
                                        x = chess_board.GameBoard + colonne * chess_board.Square + chess_board.Square // 2
                                        y = ligne * chess_board.Square + chess_board.Square // 2
                                        pygame.draw.circle(game_win, (0, 255, 255), (x, y), chess_board.Square // 6)
                                    pygame.display.update()
                                else:
                                    texte = "Choisissez une pièce valide"
                                if isinstance(piece, Cavalier):
                                    deplacements_possibles = piece.deplacements_possibles(position, chess_board)
                                    for d in deplacements_possibles:
                                        ligne, colonne = d
                                        x = chess_board.GameBoard + colonne * chess_board.Square + chess_board.Square // 2
                                        y = ligne * chess_board.Square + chess_board.Square // 2
                                        pygame.draw.circle(game_win, (0, 255, 255), (x, y), chess_board.Square // 6)
                                    pygame.display.update()
                                if isinstance(piece, Tour):
                                    deplacements_possibles = piece.deplacements_possibles(position, chess_board)
                                    for d in deplacements_possibles:
                                        ligne, colonne = d
                                        x = chess_board.GameBoard + colonne * chess_board.Square + chess_board.Square // 2
                                        y = ligne * chess_board.Square + chess_board.Square // 2
                                        pygame.draw.circle(game_win, (0, 255, 255), (x, y), chess_board.Square // 6)
                                    pygame.display.update()
                                if isinstance(piece, Fou):
                                    deplacements_possibles = piece.deplacements_possibles(position, chess_board)
                                    for d in deplacements_possibles:
                                        ligne, colonne = d
                                        x = chess_board.GameBoard + colonne * chess_board.Square + chess_board.Square // 2
                                        y = ligne * chess_board.Square + chess_board.Square // 2
                                        pygame.draw.circle(game_win, (0, 255, 255), (x, y), chess_board.Square // 6)
                                    pygame.display.update()
                                if isinstance(piece, Roi):
                                    deplacements_possibles = piece.deplacements_possibles(position, chess_board)
                                    for d in deplacements_possibles:
                                        ligne, colonne = d
                                        x = chess_board.GameBoard + colonne * chess_board.Square + chess_board.Square // 2
                                        y = ligne * chess_board.Square + chess_board.Square // 2
                                        pygame.draw.circle(game_win, (0, 255, 255), (x, y), chess_board.Square // 6)
                                    pygame.display.update()
                                if isinstance(piece, Reine):
                                    deplacements_possibles = piece.deplacements_possibles(position, chess_board)
                                    for d in deplacements_possibles:
                                        ligne, colonne = d
                                        x = chess_board.GameBoard + colonne * chess_board.Square + chess_board.Square // 2
                                        y = ligne * chess_board.Square + chess_board.Square // 2
                                        pygame.draw.circle(game_win, (0, 255, 255), (x, y), chess_board.Square // 6)
                                    pygame.display.update()
                            except:
                                texte ="Choisissez une pièce"
                        else:
                            if piece and piece.couleur == chess_board.current_player:
                                echec_manager.est_mouvement_valide_resout_echec(piece, position)
                                
                                clientChat.send_message(str(positionpiece)+str(position))
                            else:
                                texte ="Sélectionnez une pièce valide."
                            waiting_for_second_click = False
                    time.sleep(0.6)
            
            
            chess_board.draw_Board()
            chess_board.draw_pieces()
            # Dessiner les boutons
            play_button_rect, settings_button_rect, quit_button_rect = draw_buttons(game_win)
            # Afficher le bouton son
            bouton_son.afficher(game_win, True)
            pygame.display.flip()
            pygame.display.update()
            



    except KeyboardInterrupt:
        clientChat.close()
        print("Client closed")
    # interface = interface.GameInterface(game)
    # interface.runGameLoop()
    # print("end")


if __name__ == "__main__":

    main()
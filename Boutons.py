import pygame


class Boutons:
    def __init__(self, win, nom, coordonnee, taille, fct):
        self.win = win
        self.nom = nom
        self.coordonnee = coordonnee
        self.taille = taille
        self.visible = None

    def afficher(self, win, main_button):
        if main_button == True :
            draw_buttons(win)

    def cacher(self, win, main_button):
        if main_button == True :
            black_rect1 = pygame.Rect(50, 200, 200, 50)
            black_rect2 = pygame.Rect(50, 300, 200, 50)
            black_rect3 = pygame.Rect(50, 400, 200, 50)
            pygame.draw.rect(win, (0, 0, 0), (50, 200, 200, 50))
            pygame.draw.rect(win, (255, 255, 255), black_rect2)
            pygame.draw.rect(win, (255, 255, 255), black_rect3)

def draw_buttons_test(self):
    font = pygame.font.Font(None, 36)
    # Bouton
    play_button_rect = pygame.Rect(self.coordonnee)
    pygame.draw.rect(self.win, (0, 255, 0), play_button_rect)
    play_text = font.render(self.nom, True, (0, 0, 0))
    self.win.blit(play_text, (
        play_button_rect.centerx - play_text.get_width() // 2,
        play_button_rect.centery - play_text.get_height() // 2))
def draw_buttons(win):
    font = pygame.font.Font(None, 36)
    # Bouton "Jouer"
    play_button_rect = pygame.Rect(50, 200, 200, 50)
    pygame.draw.rect(win, (0, 255, 0), play_button_rect)
    play_text = font.render("Jouer", True, (0, 0, 0))
    win.blit(play_text, (
    play_button_rect.centerx - play_text.get_width() // 2, play_button_rect.centery - play_text.get_height() // 2))
    # Bouton "Paramètre"
    settings_button_rect = pygame.Rect(50, 300, 200, 50)
    pygame.draw.rect(win, (255, 255, 0), settings_button_rect)
    settings_text = font.render("ON/OFF Son", True, (0, 0, 0))
    win.blit(settings_text, (settings_button_rect.centerx - settings_text.get_width() // 2,
                             settings_button_rect.centery - settings_text.get_height() // 2))
    # Bouton "Quitter"
    quit_button_rect = pygame.Rect(50, 400, 200, 50)
    pygame.draw.rect(win, (255, 0, 0), quit_button_rect)
    quit_text = font.render("Quitter", True, (0, 0, 0))
    win.blit(quit_text, (
    quit_button_rect.centerx - quit_text.get_width() // 2, quit_button_rect.centery - quit_text.get_height() // 2))
    return play_button_rect, settings_button_rect, quit_button_rect
def draw_sub_buttons(win):
    font = pygame.font.Font(None, 36)
    # Sous-Bouton "Joueur vs Joueur"
    P1vsP2_button_rect = pygame.Rect(50, 200, 200, 50)
    pygame.draw.rect(win, (0, 255, 0), P1vsP2_button_rect)
    play_text = font.render("Joueur vs Joueur", True, (0, 0, 0))
    win.blit(play_text, (
        P1vsP2_button_rect.centerx - play_text.get_width() // 2, P1vsP2_button_rect.centery - play_text.get_height() // 2))
    # Sous-Bouton "Joueur vs IA"
    IA_button_rect = pygame.Rect(50, 250, 200, 50)
    pygame.draw.rect(win, (0, 255, 0), IA_button_rect)
    play_text = font.render("Joueur vs IA", True, (0, 0, 0))
    win.blit(play_text, (
        IA_button_rect.centerx - play_text.get_width() // 2, IA_button_rect.centery - play_text.get_height() // 2))
def draw_return_button(win):
    font = pygame.font.Font(None, 36)
    # Bouton "Retour"
    return_button_rect = pygame.Rect(50, 350, 200, 50)
    pygame.draw.rect(win, (255, 0, 0), return_button_rect)
    return_text = font.render("Retour", True, (0, 0, 0))
    win.blit(return_text, (
        return_button_rect.centerx - return_text.get_width() // 2, return_button_rect.centery - return_text.get_height() // 2))

class BoutonSon(Boutons):
    def __init__(self, win, nom, coordonnee, taille, fct):
        super().__init__(win, nom, coordonnee, taille, fct)
        self.son_active = True  # Ajoutez un attribut pour suivre l'état du son

    def gerer_son(self):
        # Fonction pour activer ou désactiver le son
        self.son_active = not self.son_active
        print(f"Son {'activé' if self.son_active else 'désactivé'}")

    def afficher(self, win, main_button):
        # Surchargez la fonction afficher pour inclure la gestion du son
        super().afficher(win, main_button)

        if main_button == True:
            draw_buttons(win)

            pygame.draw.rect(win, (0, 0, 0), (100, 50, 200, 30))
            # Afficher l'état actuel du son
            son_text = "Son: Activé" if self.son_active else "Son: Désactivé"
            font = pygame.font.Font(None, 30)
            text = font.render(son_text, True, (255, 255, 255))
            win.blit(text, (100, 50))

import pygame
def draw_buttons(win, show_P1vsP2_button, show_IA_button):
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
    settings_text = font.render("Paramètre", True, (0, 0, 0))
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
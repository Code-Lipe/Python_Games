import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Uma classe que representa um único alienígena da frota"""

    def __init__(self, settings, screen):
        """Inicializa o alienígena e define sua posição incial"""
        super(Alien, self).__init__()
        self.screen = screen
        self.settings = settings

        # Carrega a imgagem do alienígena e define seu atriburo rect
        self.image = pygame.image.load('alien_invasion/images/alien.bmp')
        self.rect = self.image.get_rect()

        # Inicia cada novo alienígena próximo à parte superior esquerda da tela
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Armazena a posição exata do alienígena
        self.x = float(self.rect.x)

    
    def blitme(self):
        """Desenha o alienígena em sua posição atual"""
        self.screen.blit(self.image, self.rect)

    
    def check_edges(self):
        """Devolve True se o alienígena estiver na borda da tela."""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        
        elif self.rect.left <= 0:
            return True


    def update(self):
        """Move o alienígena para a direita"""
        self.x += self.settings.alien_speed_factor * self.settings.fleet_direction
        self.rect.x = self.x

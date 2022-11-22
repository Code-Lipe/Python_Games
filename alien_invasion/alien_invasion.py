import pygame
from pygame.sprite import Group 
from settings import Settings
from game_stats import GameStarts
from scoreboard import Scoreboard
from button import Button
from ship import Ship
import game_functions as gf

def run_game():
    # Inicializa o pygame, as configuraçõe e o objeto screen
    pygame.init()
    settings = Settings()

    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

    pygame.display.set_caption("Alien Invasion")

    # Cria o botão Play
    play_button = Button(settings, screen, "Play")

    # Cria uma instância para armazenar dados estatísticos do jogo
    stats = GameStarts(settings)
    sb = Scoreboard(settings, screen, stats)

    # Cria uma espaçonave, um grupo de projéteis e um grupo de alienígenas
    ship = Ship(settings, screen)
    bullets = Group()
    aliens = Group()

    # Cria a frota de alienígenas
    gf.create_fleet(settings, screen, ship, aliens)

    # Inicia o laço principal do jogo
    while True:
        gf.check_events(settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            gf.update_bullets(settings, screen, stats, sb, ship, 
            aliens, bullets)
            gf.update_aliens(settings, screen, stats, sb, ship, aliens, bullets)

        gf.update_screen(settings, screen, stats, sb, ship, aliens, bullets, play_button)


run_game()

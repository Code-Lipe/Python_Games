class GameStarts():
    """Armazena dados estatíticos da invasão alienígena"""

    def __init__(self, settings):
        """Inicializa os dados estatísticos"""
        self.settings = settings
        self.reset_stats()

        # inicia a invasão alienígena em um estado ativo
        self.game_active = False

        # A pontuação máxima jamais deverá ser reiniciada
        self.high_score = 0

    
    def reset_stats(self):
        """Inicializa os dados estatíticos que podem mudar durante o jogo."""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1
        
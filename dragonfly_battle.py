import pygame as pg
import sys

from settings import Settings
from dragonfly import Dragonfly


class DragonflyBattle:
    """Класс для управления поведением игры 'Битва стрекозы'."""

    def __init__(self):
        pg.init()

        self.settings = Settings()
        self.screen = pg.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
            )

        pg.display.set_caption("Dragonfly battle!")
        self.dragonfly = Dragonfly(self.screen)

    def run_game(self):
        """Запуск основной игры."""

        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
        """Обрабатывает нажатие клавиш."""

        for event in pg.event.get():
            if event.type == pg.QUIT:
                sys.exit()

    def _update_screen(self):
        """Обновляет изображение."""

        self.screen.fill(self.settings.bg_color)
        self.dragonfly.paint_dragonfly()

        pg.display.flip()


if __name__ == '__main__':
    df = DragonflyBattle()
    df.run_game()






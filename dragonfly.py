import pygame as pg


class Dragonfly:
    """Класс для управления стрекозой."""

    def __init__(self, window):
        # Получаем экран и изображение
        self.screen = window
        self.image = pg.image.load('images/dragonfly.bmp')

        # Подгоняем всё в прямоугольный формат.
        self.screen_rect = window.get_rect()
        self.image_rect = self.image.get_rect()

        # Определяем позицию корабля.
        self.image_rect.midbottom = self.screen_rect.midbottom

    def paint_dragonfly(self):
        """Рисует стрекозу."""
        self.screen.blit(self.image, self.image_rect)







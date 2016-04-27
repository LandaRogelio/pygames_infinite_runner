import pygame


class Box(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface([80, 80])
        self.image.fill(pygame.Color(0, 0, 0))
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.y = y
        self.rect.x = x

    def move(self, inc):
        self.rect.x -= inc
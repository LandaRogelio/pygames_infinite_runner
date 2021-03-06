import pygame
import random


class Platforms(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.x_mult = random.randint(15, 20)
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        self.image = pygame.Surface([self.x_mult*50, 400])
        self.image.fill(pygame.Color(255, 255, 255))
        self.rect = self.image.get_rect()
        self.image.fill(pygame.Color(r, g, b), self.rect.inflate(-5, -5))
        self.x = x
        self.y = y * random.uniform(0.4, 1.0)
        self.rect.y = y * random.uniform(0.4, 1.0)
        self.rect.x = x
        self.has_enemy = random.randint(0, 2)
        self.has_collect = random.randint(0, 2)
        self.has_ghost = random.randint(0, 2)
        self.size = self.image.get_width()
        self.checkpoint = False

    def move(self, inc):
        self.rect.x -= inc


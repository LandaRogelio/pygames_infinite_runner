import pygame
import math
import random
from pygames_infinite_runner.spritesheet_functions import SpriteSheet


class Background:
    def __init__(self):
        super().__init__()
        self.curr_color = [random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)]
        self.target_color = [random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)]
        self.speed = 2

    def update(self):
        if int(math.ceil(self.curr_color[0]) - 1) == self.target_color[0]:
            self.target_color = [random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)]
        elif int(math.ceil(self.curr_color[0]) + 1) == self.target_color[0]:
            self.target_color = [random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)]

        self.curr_color = self.transition3(self.speed, 255, self.curr_color, self.target_color)

    def debug(self):
        print(self.curr_color, self.target_color)

    def transition(self, value, max_val, start, end):
        return start + (end - start) * value / max_val

    def transition3(self, value, max_val, rgb1, rgb2):
        r1 = self.transition(value, max_val, rgb1[0], rgb2[0])
        r2 = self.transition(value, max_val, rgb1[1], rgb2[1])
        r3 = self.transition(value, max_val, rgb1[2], rgb2[2])
        r = [r1, r2, r3]
        return r


class Cloud(pygame.sprite.Sprite):
    scale = [1, 1.3, 1.6, 2]

    def __init__(self):
        super().__init__()
        sprite_sheet = SpriteSheet('sprites/cloud.png')
        self.image = sprite_sheet.get_image(0, 0, 384, 288)
        self.image.set_alpha(80)
        scale_index = random.randint(0, len(self.scale)-1)
        self.image = pygame.transform.scale(self.image, (int(384/self.scale[scale_index]),
                                                         int(288/self.scale[scale_index])))
        self.rect = self.image.get_rect()
        self.x = random.randint(800, 1200)
        self.y = random.randint(-100, 100)
        self.rect.y = self.y
        self.rect.x = self.x

    def move(self, inc):
        self.rect.x -= inc
import pygame
from pygames_infinite_runner.spritesheet_functions import SpriteSheet


class Ghost(pygame.sprite.Sprite):
    ghost_frames = []
    time = 0

    def __init__(self, x, y):
        super().__init__()
        sprite_sheet = SpriteSheet('sprites/ghost.png')
        self.image = sprite_sheet.get_image(43, 29, 48, 48)
        self.ghost_frames.append(self.image)
        self.image = sprite_sheet.get_image(165, 29, 48, 48)
        self.ghost_frames.append(self.image)
        self.image = sprite_sheet.get_image(287, 29, 48, 48)
        self.ghost_frames.append(self.image)
        self.image = sprite_sheet.get_image(408, 29, 48, 48)
        self.ghost_frames.append(self.image)
        self.image = sprite_sheet.get_image(530, 29, 48, 48)
        self.ghost_frames.append(self.image)
        self.image = sprite_sheet.get_image(652, 29, 48, 48)
        self.ghost_frames.append(self.image)
        self.rect = self.image.get_rect()

        self.curr_frame = 0
        self.image = self.ghost_frames[self.curr_frame]

        self.x = x
        self.y = y
        self.rect.y = y
        self.rect.x = x

    def move(self, inc):
        self.rect.x -= inc

    def update(self):
        self.time += .5
        if self.time % 2 == 0:
            if self.curr_frame >= len(self.ghost_frames)-1:
                self.curr_frame = 0
            else:
                self.curr_frame += 1

        self.image = self.ghost_frames[self.curr_frame]
        self.image.set_alpha(90)

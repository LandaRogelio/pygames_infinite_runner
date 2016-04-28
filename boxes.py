import pygame
from pygames_infinite_runner.spritesheet_functions import SpriteSheet


class Box(pygame.sprite.Sprite):
    stance_frames = []
    time = 0

    def __init__(self, x, y):
        super().__init__()
        #self.image = pygame.Surface([80, 80])
        #self.image.fill(pygame.Color(0, 0, 0))
        sprite_sheet = SpriteSheet("sprites/enemy_sheet.png")
        self.image = sprite_sheet.get_image(27, 10, 40, 71)
        self.image = pygame.transform.flip(self.image, True, False)
        self.stance_frames.append(self.image)
        self.image = sprite_sheet.get_image(137, 10, 40, 71)
        self.image = pygame.transform.flip(self.image, True, False)
        self.stance_frames.append(self.image)
        self.image = sprite_sheet.get_image(247, 10, 40, 71)
        self.image = pygame.transform.flip(self.image, True, False)
        self.stance_frames.append(self.image)
        self.image = sprite_sheet.get_image(357, 10, 40, 71)
        self.image = pygame.transform.flip(self.image, True, False)
        self.stance_frames.append(self.image)
        self.image = sprite_sheet.get_image(467, 10, 40, 71)
        self.image = pygame.transform.flip(self.image, True, False)
        self.stance_frames.append(self.image)
        self.image = sprite_sheet.get_image(577, 10, 40, 71)
        self.image = pygame.transform.flip(self.image, True, False)
        self.stance_frames.append(self.image)
        self.image = sprite_sheet.get_image(687, 10, 40, 71)
        self.image = pygame.transform.flip(self.image, True, False)
        self.stance_frames.append(self.image)
        self.image = sprite_sheet.get_image(797, 10, 40, 71)
        self.image = pygame.transform.flip(self.image, True, False)
        self.stance_frames.append(self.image)
        self.image = sprite_sheet.get_image(907, 10, 40, 71)
        self.image = pygame.transform.flip(self.image, True, False)
        self.stance_frames.append(self.image)
        self.rect = self.image.get_rect()
        self.image = sprite_sheet.get_image(1017, 10, 40, 71)
        self.image = pygame.transform.flip(self.image, True, False)
        self.stance_frames.append(self.image)
        self.image = sprite_sheet.get_image(1127, 10, 40, 71)
        self.image = pygame.transform.flip(self.image, True, False)
        self.stance_frames.append(self.image)
        self.image = sprite_sheet.get_image(1237, 10, 40, 71)
        self.image = pygame.transform.flip(self.image, True, False)
        self.stance_frames.append(self.image)
        self.image = sprite_sheet.get_image(1347, 10, 40, 71)
        self.image = pygame.transform.flip(self.image, True, False)
        self.stance_frames.append(self.image)
        self.image = sprite_sheet.get_image(1457, 10, 40, 71)
        self.image = pygame.transform.flip(self.image, True, False)
        self.stance_frames.append(self.image)

        self.curr_frame = 0
        self.image = self.stance_frames[self.curr_frame]
        self.x = x
        self.y = y
        self.rect.y = y
        self.rect.x = x

    def move(self, inc):
        self.rect.x -= inc

    def update(self):
        self.time += .5
        if self.time % 2 == 0:
                if self.curr_frame >= len(self.stance_frames)-1:
                    self.curr_frame = 0
                else:
                    self.curr_frame += 1

        self.image = self.stance_frames[self.curr_frame]

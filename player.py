import pygame
from pygames_infinite_runner.spritesheet_functions import SpriteSheet
import pygames_infinite_runner.constants as constants


class Player(pygame.sprite.Sprite):
    # -- Attributes
    # Set speed vector of player
    change_y = 0

    walking_frames_r = []
    charge_frames = []
    fire_frames = []
    time = 0
    boost_timer = 8
    platform_list = None
    collect_list = None
    box_list = None

    num_jumps = 0
    jumping = False
    falling = False
    boosting = False

    # -- Methods
    def __init__(self, x, y):
        """ Constructor function """

        self.x = x
        self.y = y
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)

        """sprite_sheet = SpriteSheet("p1_walk.png")
        # Load all the right facing images into a list
        image = sprite_sheet.get_image(0, 0, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(66, 0, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(132, 0, 67, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(0, 93, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(66, 93, 66, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(132, 93, 72, 90)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(0, 186, 70, 90)
        self.walking_frames_r.append(image)
        """
        sprite_sheet = SpriteSheet("sprite_walk.png")
        image = sprite_sheet.get_image(0, 0, 40, 60)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(40, 0, 40, 60)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(80, 0, 40, 60)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(120, 0, 40, 60)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(160, 0, 40, 60)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(200, 0, 40, 60)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(240, 0, 40, 60)
        self.walking_frames_r.append(image)
        image = sprite_sheet.get_image(280, 0, 40, 60)
        self.walking_frames_r.append(image)

        image = sprite_sheet.get_image(0, 120, 40, 60)
        self.charge_frames.append(image)
        image = sprite_sheet.get_image(40, 120, 40, 60)
        self.charge_frames.append(image)
        image = sprite_sheet.get_image(80, 120, 40, 60)
        self.charge_frames.append(image)
        image = sprite_sheet.get_image(120, 120, 40, 60)
        self.charge_frames.append(image)
        image = sprite_sheet.get_image(160, 120, 40, 60)
        self.charge_frames.append(image)
        image = sprite_sheet.get_image(200, 120, 40, 60)
        self.charge_frames.append(image)
        image = sprite_sheet.get_image(240, 120, 40, 60)
        self.charge_frames.append(image)
        image = sprite_sheet.get_image(280, 120, 40, 60)
        self.charge_frames.append(image)

        image = sprite_sheet.get_image(0, 60, 40, 60)
        self.jumping_sprite = image
        image = sprite_sheet.get_image(40, 60, 40, 60)
        self.falling_sprite = image

        image = sprite_sheet.get_image(80, 60, 80, 60)
        self.fire_frames.append(image)
        image = sprite_sheet.get_image(160, 60, 80, 60)
        self.fire_frames.append(image)
        self.curr_fire_frame = 0

        # Set the image the player starts with
        self.curr_img = 0
        self.curr_boost_img = 0
        self.image = self.walking_frames_r[self.curr_img]

        # Set a reference to the image rect.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.calc_gravity()
        self.time += .25

        if self.time % 2 == 0:
            if self.curr_img >= len(self.walking_frames_r)-1:
                self.curr_img = 0
            else:
                self.curr_img += 1

        if self.time * 4 % 2 == 0:
            if self.curr_boost_img >= len(self.charge_frames)-1:
                self.curr_boost_img = 0
            else:
                self.curr_boost_img += 1
            if self.curr_fire_frame >= len(self.fire_frames)-1:
                self.curr_fire_frame = 0
            else:
                self.curr_fire_frame += 1

        if self.jumping:
            self.image = self.jumping_sprite
        elif self.falling:
            self.image = self.falling_sprite
        else:
            self.image = self.walking_frames_r[self.curr_img]

        if self.boosting:
            self.image = self.charge_frames[self.curr_boost_img]

        if self.boosting:
            self.boost_timer -= 0.5
        if self.boost_timer < 0:
            self.boosting = False
            self.boost_timer = 8

        # Move up/down
        self.rect.y += self.change_y

        collect_hit_list = pygame.sprite.spritecollide(self, self.collect_list, True)

        if self.boosting:
            box_hit_list = pygame.sprite.spritecollide(self, self.box_list, True)
        else:
            box_hit_list = pygame.sprite.spritecollide(self, self.box_list, False)


        block_hit_list = pygame.sprite.spritecollide(self, self.platform_list, False)
        for block in block_hit_list:
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            # Stop our vertical movement
            self.change_y = 0

            self.num_jumps = 0
            self.jumping = False
            self.falling = False

        if self.change_y > 0:
            self.falling = True
            self.jumping = False

    def draw(self, screen):
        if self.boosting:
            flame = self.fire_frames[self.curr_fire_frame]
            screen.blit(flame, (self.rect.x-60, self.rect.y))

        screen.blit(self.image, (self.rect.x, self.rect.y))

    def calc_gravity(self):
        if self.change_y == 0:
            self.change_y = 1
        else:
            self.change_y += .25

        # See if we are on the ground.
        if self.rect.y >= constants.SCREEN_HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = constants.SCREEN_HEIGHT - self.rect.height

    def jump(self):
        """ Called when user hits 'jump' button. """

        # move down a bit and see if there is a platform below us.
        # Move down 2 pixels because it doesn't work well if we only move down 1
        # when working with a platform moving down.
        self.rect.y += 2
        platform_hit_list = pygame.sprite.spritecollide(self, self.platform_list, False)
        self.rect.y -= 2

        if len(platform_hit_list) > 0 or self.rect.bottom >= constants.SCREEN_HEIGHT:
            self.num_jumps = 0
            self.jumping = False
            self.falling = False

        if self.num_jumps < 2:
            self.num_jumps += 1
            self.change_y = -10
            self.curr_img = 0
            self.jumping = True

    def boost(self):
        if not self.boosting:
            self.boosting = True
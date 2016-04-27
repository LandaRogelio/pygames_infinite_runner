import pygame
import sys
from pygames_infinite_runner.platforms import Platforms
from pygames_infinite_runner.boxes import Box
from pygames_infinite_runner.collectables import Collectable
from pygames_infinite_runner.player import Player
import pygames_infinite_runner.constants as constants
from pygame.locals import *


def main():

    pygame.init()

    fps = 60
    fps_clock = pygame.time.Clock()

    window_size = (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
    SURFACE = pygame.display.set_mode(window_size)

    pygame.display.set_caption("Drawing with PyGame")

    NIGHT = pygame.Color(70, 65, 120)
    GRAY = [95, 75, 75]

    SURFACE.fill(NIGHT)

    player = Player(50, 210)
    player.draw(SURFACE)

    platform_list = pygame.sprite.Group()
    platform_list.add(Platforms(10, 500))
    box_list = pygame.sprite.Group()
    collect_list = pygame.sprite.Group()
    plat_move_speed = 8

    boost_timer = -1
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == QUIT:
                done = True
            if event.type == USEREVENT+1 and boost_timer > 0:
                boost_timer -= 1

            if event.type == KEYDOWN:
                if event.key == K_z:
                    player.jump()
                if event.key == K_x:
                    player.boost()
                    if boost_timer < 0:
                        pygame.time.set_timer(USEREVENT+1, 400)
                        boost_timer = 1
                        plat_move_speed *= 2

        SURFACE.fill(NIGHT)

        player.draw(SURFACE)
        player.platform_list = platform_list
        player.collect_list = collect_list
        player.box_list = box_list
        player.update()

        if boost_timer == 0:
            plat_move_speed /= 2
            boost_timer = -1

        platform_list.draw(SURFACE)
        box_list.draw(SURFACE)
        collect_list.draw(SURFACE)
        for item in platform_list:
            if item.rect.x == constants.SCREEN_WIDTH and (item.has_collect == 1 or item.has_collect == 2):
                collect_list.add(Collectable(item.rect.x + item.size + 400, item.rect.y-210))
            if item.rect.x == constants.SCREEN_WIDTH and (item.has_box == 1 or item.has_box == 2):
                box_list.add(Box(item.rect.x + item.size/2, item.rect.y-80))
            item.move(plat_move_speed)
            if item.rect.x + (item.x_mult*50) < 30 and not item.checkpoint:
                platform_list.add(Platforms(800, 500))
                item.checkpoint = True
            if item.rect.x + (item.x_mult*50) < 0:
                platform_list.remove(item)

        for box in box_list:
            box.move(plat_move_speed)
            if box.rect.x + 80 < 0:
                box_list.remove(box)

        for collect in collect_list:
            collect.move(plat_move_speed)
            if collect.rect.x + 10 < 0:
                collect_list.remove(collect)

        pygame.display.flip()
        fps_clock.tick(fps)

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()


if __name__ == "__main__":
    main()

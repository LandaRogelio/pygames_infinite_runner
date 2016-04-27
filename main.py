import pygame
import sys
from pygames_infinite_runner.platforms import Platforms
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
                        plat_move_speed *= 3

        SURFACE.fill(NIGHT)

        player.draw(SURFACE)
        player.platform_list = platform_list
        player.update()

        if boost_timer == 0:
            plat_move_speed /= 3
            boost_timer = -1

        platform_list.draw(SURFACE)
        for item in platform_list:
            item.move(plat_move_speed)
            if item.rect.x + (item.x_mult*50) < 30 and not item.checkpoint:
                platform_list.add(Platforms(800, 500))
                item.checkpoint = True
            if item.rect.x + (item.x_mult*50) < 0:
                platform_list.remove(item)

        pygame.display.flip()
        fps_clock.tick(fps)

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()


if __name__ == "__main__":
    main()

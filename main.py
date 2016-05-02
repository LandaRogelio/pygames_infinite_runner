import pygame
import sys
from pygames_infinite_runner.platforms import Platforms
from pygames_infinite_runner.boxes import Box
from pygames_infinite_runner.collectables import Collectable
from pygames_infinite_runner.player import Player
import pygames_infinite_runner.constants as constants
from pygame.locals import *
from itertools import repeat
import math
import random


def shake():
    s = -1
    for _ in range(0, 3):
        for x in range(10, 30, 5):
            yield (0, x*s)
        for x in range(30, 10, 5):
            yield (0, x*s)
        s *= -1
    while True:
        yield (0, 0)


def main():
    pygame.mixer.pre_init(44100, -16, 1, 512)
    pygame.init()

    fps = 60
    fps_clock = pygame.time.Clock()

    window_size = (constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)

    org_screen = pygame.display.set_mode(window_size)
    SURFACE = org_screen.copy()
    #surface_rect = SURFACE.get_rect()

    # #Load background music
    pygame.mixer.music.load('music/Visager_Battle_Loop.mp3')
    pygame.mixer.music.set_volume(.3)
    pygame.mixer.music.set_endevent(USEREVENT + 4)
    pygame.mixer.music.play()

    pygame.display.set_caption("Drawing with PyGame")

    mana_font = pygame.font.Font('fonts/manaspc.ttf', 30)
    sm_mana_font = pygame.font.Font('fonts/manaspc.ttf', 20)

    SURFACE.fill(constants.NIGHT)

    player = Player(50, 210)
    player.draw(SURFACE)

    platform_list = pygame.sprite.Group()
    platform_list.add(Platforms(10, 500))
    box_list = pygame.sprite.Group()
    collect_list = pygame.sprite.Group()
    plat_move_speed = 6
    plat_move_mult = 1

    offset = repeat((0, 0))
    boost_timer = -1
    done = False
    lose = False
    time = 0
    mult = 1
    add_points = 0

    while not done:
        for event in pygame.event.get():
            if event.type == QUIT:
                done = True
            if event.type == USEREVENT+1 and boost_timer > 0:
                boost_timer -= 1
                pygame.time.set_timer(USEREVENT+1, 0)
            if event.type == USEREVENT+0:
                plat_move_speed = 0
                offset = shake()
                lose = True
                pygame.time.set_timer(USEREVENT+0, 0)
            if event.type == USEREVENT+2:
                pygame.time.set_timer(USEREVENT+2, 0)
                add_points = 20 * mult
                pygame.time.set_timer(USEREVENT+5, 500)
                offset = shake()
            if event.type == USEREVENT + 3:
                pygame.time.set_timer(USEREVENT+3, 0)
                add_points = 10 * mult
                pygame.time.set_timer(USEREVENT+5, 500)
            if event.type == USEREVENT + 4:
                pygame.mixer.music.play()
            if event.type == USEREVENT + 5:
                pygame.time.set_timer(USEREVENT+5, 0)
                add_points = 0

            if event.type == KEYDOWN:
                if event.key == K_z:
                    player.jump()
                if event.key == K_x:
                    player.boost()
                    if boost_timer < 0:
                        pygame.time.set_timer(USEREVENT+1, 400)
                        boost_timer = 1
                        plat_move_mult = 2

        SURFACE.fill(constants.NIGHT)

        player.draw(SURFACE)
        player.platform_list = platform_list
        player.collect_list = collect_list
        player.box_list = box_list
        player.update(mult)

        if boost_timer == 0:
            plat_move_mult= 1
            boost_timer = -1

        platform_list.draw(SURFACE)
        box_list.draw(SURFACE)
        collect_list.draw(SURFACE)

        for item in platform_list:
            if item.rect.x == constants.SCREEN_WIDTH and (item.has_collect == 1 or item.has_collect == 2):
                collect_list.add(Collectable(item.rect.x + item.size + 400, item.rect.y-210))
            if item.rect.x == constants.SCREEN_WIDTH and (item.has_box == 1 or item.has_box == 2):
                box_list.add(Box(item.rect.x + item.size/2, item.rect.y-71, random.randint(0, 1)))
            item.move(plat_move_speed)
            if item.rect.x + (item.x_mult*50) < 30 and not item.checkpoint:
                platform_list.add(Platforms(800, 500))
                item.checkpoint = True
            if item.rect.x + (item.x_mult*50) < 0:
                platform_list.remove(item)

        for box in box_list:
            box.move(plat_move_speed)
            box.update()
            if box.rect.x + 80 < 0:
                box_list.remove(box)

        for collect in collect_list:
            collect.move(plat_move_speed)
            if collect.rect.x + 10 < 0:
                collect_list.remove(collect)

        time_passed = fps_clock.tick(fps)
        time_passed_seconds = time_passed / 1000.0
        if not lose:
            time += time_passed_seconds

        score_render = mana_font.render(str(math.floor(player.score)), False, (255, 255, 255))
        mult_render = sm_mana_font.render('X' + str(mult), False, (255, 255, 255))
        time_render = mana_font.render(str(math.floor(time)), False, (255, 255, 255))
        point_render = sm_mana_font.render('+' + str(math.floor(add_points)), False, (255, 255, 255))

        if time > 90.0 and not lose:
            if plat_move_mult == 2:
                plat_move_mult = 1.5
            plat_move_speed = 18 * plat_move_mult
            player.gravity = 0.35
            mult = 10
            if boost_timer < 0:
                player.score += time_passed_seconds * 20
        elif time > 75.0 and not lose:
            if plat_move_mult == 2:
                plat_move_mult = 1.7
            plat_move_speed = 16 * plat_move_mult
            player.gravity = 0.30
            mult = 8
            if boost_timer < 0:
                player.score += time_passed_seconds * 16
        elif time > 60.0 and not lose:
            plat_move_speed = 14 * plat_move_mult
            player.gravity = 0.25
            mult = 6
            if boost_timer < 0:
                player.score += time_passed_seconds * 12
        elif time > 45.0 and not lose:
            plat_move_speed = 12 * plat_move_mult
            mult = 4
            if boost_timer < 0:
                player.score += time_passed_seconds * 8
        elif time > 30.0 and not lose:
            plat_move_speed = 10 * plat_move_mult
            mult = 2
            if boost_timer < 0:
                player.score += time_passed_seconds * 4
        elif time > 10.0 and not lose:
            plat_move_speed = 8 * plat_move_mult
            mult = 1.5
            if boost_timer < 0:
                player.score += time_passed_seconds * 3
        elif 9.0 > time > 0.0:
            plat_move_speed = 6 * plat_move_mult
            if boost_timer < 0:
                player.score += time_passed_seconds * 2

        if add_points != 0:
            SURFACE.blit(point_render, (player.rect.x + 15, player.rect.y - 30))
        SURFACE.blit(score_render, (constants.SCREEN_WIDTH/2, 20))
        if mult != 1:
            SURFACE.blit(mult_render, (constants.SCREEN_WIDTH/2, 50))
        SURFACE.blit(time_render, (20, 20))
        org_screen.blit(SURFACE, next(offset))
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()


if __name__ == "__main__":
    main()

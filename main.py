import sys

import pygame
from pygame.locals import *

from ball import Ball
from separator import Separator
from player import Player

pygame.init()

screen_width = 800
screen_height = 600
caption = "PONG"

number_text_size = 72
text_size = 32

number_font = pygame.font.Font("font.ttf", number_text_size)
text_font = pygame.font.Font("font.ttf", text_size)

max_score = 5

game_display = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(caption)

clock = pygame.time.Clock()

white = (230, 230, 230)
black = (40, 40, 40)

start_text = text_font.render("Press Space to start", True, white)


def check_collision_player(player, ball_object):
    if player.get_id() == 1:
        if player.x <= ball_object.x <= player.x + player.width:
            if player.y <= ball_object.y <= player.y + player.height:
                ball_object.change_direction_player()
    else:
        if player.x <= ball_object.x <= player.x + player.width:
            if player.y <= ball_object.y <= player.y + player.height:
                ball_object.change_direction_player()


def check_collision_wall(ball_object, player1, player2):
    if ball_object.y <= 0 or ball_object.y >= screen_height - ball_object.height:
        ball_object.change_direction_wall()

    if ball_object.x <= 0:
        ball_object.__init__("right", white, screen_width, screen_height)
        player2.add_score()

    if ball_object.x >= screen_width - ball_object.width:
        ball_object.__init__("left", white, screen_width, screen_height)
        player1.add_score()


def show_score(player):
    player_score_text = number_font.render(
        str(player.get_score()), True, white)

    if player.get_id() == 1:
        game_display.blit(player_score_text, [
                          screen_width / 4 - text_size / 4, 20])
    else:
        game_display.blit(player_score_text, [
                          screen_width / 4 * 3 - text_size / 4, 20])


def player_win_actions(player, ball_object):
    if player.get_id() == 1:
        player_text = text_font.render("Player 1 wins", True, white)
    else:
        player_text = text_font.render("Player 2 wins", True, white)

    game_display.blit(player_text, [300, 200])

    ball_object.speed_x = 0
    ball_object.speed_y = 0


def player_win(player1, player2, ball_object):
    if player1.get_score() >= max_score and player1.get_score() >= player2.get_score() + 2:
        player_win_actions(player1, ball_object)
        return True

    elif player2.get_score() >= max_score and player2.get_score() >= player1.get_score() + 2:
        player_win_actions(player2, ball_object)
        return True

    return False


def quit_game():
    pygame.quit()
    sys.exit()


def main_loop():
    start = False
    game_exit = False
    game_over = False

    separator = Separator(white, screen_width)
    ball_object = Ball("none", white, screen_width, screen_height)

    player1 = Player(1, white, screen_width, screen_height)
    player2 = Player(2, white, screen_width, screen_height)

    while not game_exit:
        for event in pygame.event.get():
            if event.type == QUIT:
                game_exit = True

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    game_exit = True

                if start:
                    if event.key == K_w:
                        player1.move_up()
                    if event.key == K_s:
                        player1.move_down()

                    if event.key == K_UP:
                        player2.move_up()
                    if event.key == K_DOWN:
                        player2.move_down()

                if event.key == K_SPACE:
                    if not start:
                        start = True
                        ball_object.__init__(
                            "left", white, screen_width, screen_height)
                    if game_over:
                        main_loop()

            if event.type == KEYUP:
                if event.key == K_w or event.key == K_s:
                    player1.stop()
                if event.key == K_UP or event.key == K_DOWN:
                    player2.stop()

        game_display.fill(black)

        if start:
            ball_object.draw(game_display)
        separator.draw(game_display, screen_height)

        player1.draw(game_display, screen_height)
        player2.draw(game_display, screen_height)

        if not start and not game_over:
            game_display.blit(start_text, [240, 200])

        show_score(player1)
        show_score(player2)

        if not game_over:
            check_collision_player(player1, ball_object)
            check_collision_player(player2, ball_object)

            check_collision_wall(ball_object, player1, player2)

        if player_win(player1, player2, ball_object):
            start = False
            game_over = True

        clock.tick()
        pygame.display.update()

    quit_game()


main_loop()

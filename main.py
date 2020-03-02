import pygame
import sys
from pygame.locals import *

from ball import Ball
from player import Player
from line import Line

pygame.init()

screen_width = 800
screen_height = 600
caption = "PONG"

number_text_size = 72
text_size = 32

number_font = pygame.font.Font("font.ttf", number_text_size)
text_font = pygame.font.Font("font.ttf", text_size)

game_display = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(caption)

clock = pygame.time.Clock()

white = (230, 230, 230)
black = (40, 40, 40)

start_text = text_font.render("Press Space to start", True, white)


def quit_game():
    pygame.quit()
    sys.exit()


def main_loop():
    start = False
    game_exit = False
    game_over = False

    line = Line(white, screen_width)
    ball_object = Ball("none", white, screen_width, screen_height)

    player1 = Player(1, white, screen_width, screen_height)
    player2 = Player(2, white, screen_width, screen_height)

    player1_score = 0
    player2_score = 0

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
                        ball_object.__init__("left", white, screen_width, screen_height)
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
        line.draw(game_display, screen_height)

        player1.draw(game_display, screen_height)
        player2.draw(game_display, screen_height)

        if not start and not game_over:
            game_display.blit(start_text, [240, 200])

        player1_score_text = number_font.render(str(player1_score), True, white)
        player2_score_text = number_font.render(str(player2_score), True, white)

        game_display.blit(player1_score_text, [screen_width / 4 - text_size / 4, 20])
        game_display.blit(player2_score_text, [screen_width / 4 * 3 - text_size / 4, 20])

        if not game_over:
            if player1.x <= ball_object.x <= player1.x + player1.width:
                if player1.y <= ball_object.y <= player1.y + player1.height:
                    ball_object.change_direction_player()

            if player2.x <= ball_object.x <= player2.x + player2.width:
                if player2.y <= ball_object.y <= player2.y + player2.height:
                    ball_object.change_direction_player()

            if ball_object.y <= 0 or ball_object.y >= screen_height - ball_object.height:
                ball_object.change_direction_wall()

            if ball_object.x <= 0:
                ball_object.__init__("right", white, screen_width, screen_height)
                player2_score += 1

            if ball_object.x >= screen_width - ball_object.width:
                ball_object.__init__("left", white, screen_width, screen_height)
                player1_score += 1

        if (player1_score >= 5 and player2_score <= 3) or (player1_score >= 5 and player1_score >= player2_score + 2):
            start = False
            game_over = True

            player_text = text_font.render("Player 1 wins", True, white)
            game_display.blit(player_text, [300, 200])

            ball_object.speed_x = 0
            ball_object.speed_y = 0

        if (player2_score >= 5 and player1_score <= 3) or (player2_score >= 5 and player2_score >= player1_score + 2):
            start = False
            game_over = True

            player_text = text_font.render("Player 2 wins", True, white)
            game_display.blit(player_text, [300, 200])

            ball_object.speed_x = 0
            ball_object.speed_y = 0

        clock.tick()
        pygame.display.update()

    quit_game()


main_loop()

import sys

import pygame
from pygame.locals import *

from ball import Ball
from separator import Separator
from player import Player
from direction import Direction

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

white = (238, 238, 238)
black = (34, 40, 49)

start_text = text_font.render("Press Space to start", True, white)


# Display player scores
def display_score(player):
    player_score_text = number_font.render(
        str(player.get_score()), True, white)

    if player.get_id() == 1:
        game_display.blit(player_score_text, [
                          (int)(screen_width / 4 - text_size / 4), 20])
    else:
        game_display.blit(player_score_text, [
                          (int)(screen_width / 4 * 3 - text_size / 4), 20])


# What to do when a player wins
def player_win(player, ball):
    if player.get_id() == 1:
        player_text = text_font.render("Player 1 wins", True, white)
    else:
        player_text = text_font.render("Player 2 wins", True, white)

    game_display.blit(player_text, [300, 200])

    ball.speed_x = 0
    ball.speed_y = 0


# Return game winner when either player reaches max score
def winner(player1, player2, ball):
    if player1.get_score() >= max_score and player1.get_score() >= player2.get_score() + 2:
        return player1

    elif player2.get_score() >= max_score and player2.get_score() >= player1.get_score() + 2:
        return player2

    return None


def quit_game():
    pygame.quit()
    sys.exit()


def main_loop():
    start = False
    game_exit = False
    game_over = False

    player1 = Player(1, white, screen_width, screen_height)
    player2 = Player(2, white, screen_width, screen_height)

    ball = Ball(Direction.No, white, screen_width, screen_height)
    separator = Separator(white, screen_width)

    while not game_exit:
        for event in pygame.event.get():
            if event.type == QUIT:
                game_exit = True

            # Escape game when escape key is pressed
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    game_exit = True

                # Move players with arrow keys and WASD
                if start:
                    if event.key == K_w:
                        player1.move_up()
                    if event.key == K_s:
                        player1.move_down()

                    if event.key == K_UP:
                        player2.move_up()
                    if event.key == K_DOWN:
                        player2.move_down()

                # Press Space to start game
                if event.key == K_SPACE:
                    if not start:
                        start = True
                        ball.__init__(
                            Direction.Left, white, screen_width, screen_height)
                    if game_over:
                        main_loop()

            # Stop moving player if arrows or WASD is up
            if event.type == KEYUP:
                if event.key == K_w or event.key == K_s:
                    player1.stop()
                if event.key == K_UP or event.key == K_DOWN:
                    player2.stop()

        # Fill black background
        game_display.fill(black)

        # Render game objects and UI
        if start:
            ball.draw(game_display)
        separator.draw(game_display, screen_height)

        player1.draw(game_display, screen_height)
        player2.draw(game_display, screen_height)

        if not start and not game_over:
            game_display.blit(start_text, [240, 200])

        display_score(player1)
        display_score(player2)

        # Check collisions
        if not game_over:
            if ball.check_collision_player(player1) or ball.check_collision_player(player2):
                ball.change_direction_horizontal()

            if ball.check_collision_wall(screen_height):
                ball.change_direction_vertical()

            if ball.check_score(player1, player2, screen_width, screen_height) == player1:
                ball.__init__(Direction.Left, white,
                              screen_width, screen_height)
                player1.add_score()
            elif ball.check_score(player1, player2, screen_width, screen_height) == player2:
                ball.__init__(Direction.Right, white,
                              screen_width, screen_height)
                player2.add_score()

        # Handle game winning
        if winner(player1, player2, ball) != None:
            player_win(winner(player1, player2, ball), ball)

            start = False
            game_over = True

        clock.tick()
        pygame.display.update()

    quit_game()


main_loop()

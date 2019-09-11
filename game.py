import pygame
import sys
import random
from pygame.locals import *

pygame.init()

screen_width = 800
screen_height = 600
caption = "PONG"

text_size = 100
font = pygame.font.Font("font.ttf", text_size)

game_display = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption(caption)

white = (230, 230, 230)
black = (40, 40, 40)


class Ball:
    def __init__(self, direction):
        self.color = white

        self.width = 10
        self.height = 10

        self.x = screen_width / 2 - self.width / 2
        self.y = screen_height / 2 - self.height / 2

        self.speed = 0.3

        self.direction_horizontal = direction
        self.direction_vertical = "up"

        if self.direction_horizontal == "left":
            self.speed_x = -self.speed
        elif self.direction_horizontal == "right":
            self.speed_x = self.speed

        self.speed_y = 0

    def draw(self):
        pygame.draw.rect(game_display, self.color, [self.x, self.y, self.width, self.height])

        self.x += self.speed_x
        self.y += self.speed_y

    def change_direction_player(self):
        if self.direction_horizontal == "left":
            self.direction_horizontal = "right"
            self.speed_x = self.speed

        elif self.direction_horizontal == "right":
            self.direction_horizontal = "left"
            self.speed_x = -self.speed

        self.speed_y = random.uniform(-self.speed, self.speed)

    def change_direction_wall(self):
        if self.direction_vertical == "up":
            self.direction_vertical = "down"

        elif self.direction_vertical == "down":
            self.direction_vertical = "up"

        self.speed_y = -self.speed_y


class Player:
    def __init__(self, player_id):
        self.color = white

        self.width = 10
        self.height = 60

        self.distance = 30

        self.y = screen_height / 2 - self.height / 2
        if player_id == 1:
            self.x = self.distance
        elif player_id == 2:
            self.x = screen_width - self.distance - self.width

        self.speed = 0.5
        self.speed_y = 0

    def draw(self):
        pygame.draw.rect(game_display, self.color, [self.x, self.y, self.width, self.height])
        self.y += self.speed_y

        if self.y < 0:
            self.y = 0
        if self.y > screen_height - self.height:
            self.y = screen_height - self.height

    def move_up(self):
        self.speed_y = -self.speed

    def move_down(self):
        self.speed_y = self.speed

    def stop(self):
        self.speed_y = 0


class Line:
    def __init__(self):
        self.color = white

        self.width = 15
        self.height = 25

        self.x = screen_width / 2 - self.width / 2
        self.y = 0

    def draw(self):
        for i in range(0, screen_height, self.height + 57):
            self.y = i
            pygame.draw.rect(game_display, self.color, [self.x, self.y, self.width, self.height])


def quit_game():
    pygame.quit()
    sys.exit()


def main_loop():
    game_exit = False

    ball = Ball("left")
    line = Line()

    player1 = Player(1)
    player2 = Player(2)

    player1_score = 0
    player2_score = 0

    while not game_exit:
        for event in pygame.event.get():
            if event.type == QUIT:
                game_exit = True

            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    game_exit = True

                if event.key == K_w:
                    player1.move_up()
                if event.key == K_s:
                    player1.move_down()

                if event.key == K_UP:
                    player2.move_up()
                if event.key == K_DOWN:
                    player2.move_down()

            if event.type == KEYUP:
                if event.key == K_w or event.key == K_s:
                    player1.stop()
                if event.key == K_UP or event.key == K_DOWN:
                    player2.stop()

        game_display.fill(black)

        ball.draw()
        line.draw()

        player1.draw()
        player2.draw()

        player1_score_text = font.render(str(player1_score), True, white)
        player2_score_text = font.render(str(player2_score), True, white)

        game_display.blit(player1_score_text, [100, 20])
        game_display.blit(player2_score_text, [screen_width - 100 - text_size / 2, 20])

        if player1.x <= ball.x <= player1.x + player1.width:
            if player1.y <= ball.y <= player1.y + player1.height:
                ball.change_direction_player()

        if player2.x <= ball.x <= player2.x + player2.width:
            if player2.y <= ball.y <= player2.y + player2.height:
                ball.change_direction_player()

        if ball.y <= 0 or ball.y >= screen_height - ball.height:
            ball.change_direction_wall()

        if ball.x <= 0:
            ball.__init__("right")
            player2_score += 1

        if ball.x >= screen_width - ball.width:
            ball.__init__("left")
            player1_score += 1

        pygame.display.update()

    quit_game()


main_loop()

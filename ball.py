import pygame
import random


class Ball:
    def __init__(self, direction, color, screen_width, screen_height):
        self.color = color

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
        else:
            self.speed_x = 0

        self.speed_y = 0

    def draw(self, game_display):
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

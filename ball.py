import pygame
import random
from direction import Direction


class Ball:
    def __init__(self, direction, color, screen_width, screen_height):
        self.color = color

        self.width = 10
        self.height = 10

        self.x = screen_width / 2 - self.width / 2
        self.y = screen_height / 2 - self.height / 2

        self.speed = 1

        self.direction_horizontal = direction
        self.direction_vertical = Direction.Up

        if self.direction_horizontal == Direction.Left:
            self.speed_x = -self.speed
        elif self.direction_horizontal == Direction.Right:
            self.speed_x = self.speed
        else:
            self.speed_x = 0

        self.speed_y = 0

    def draw(self, game_display):
        pygame.draw.rect(game_display, self.color, [
                         self.x, self.y, self.width, self.height])

        self.x += self.speed_x
        self.y += self.speed_y

    def change_direction_horizontal(self):
        if self.direction_horizontal == Direction.Left:
            self.direction_horizontal = Direction.Right
            self.speed_x = self.speed

        elif self.direction_horizontal == Direction.Right:
            self.direction_horizontal = Direction.Left
            self.speed_x = -self.speed

        self.speed_y = random.uniform(-self.speed, self.speed)

    def change_direction_vertical(self):
        if self.direction_vertical == Direction.Up:
            self.direction_vertical = Direction.Down

        elif self.direction_vertical == Direction.Down:
            self.direction_vertical = Direction.Up

        self.speed_y = -self.speed_y

    def check_collision_player(self, player):
        if player.x <= self.x <= player.x + player.width:
            if player.y <= self.y <= player.y + player.height:
                return True

        return False

    def check_collision_wall(self, screen_height):
        if self.y <= 0 or self.y >= screen_height - self.height:
            return True

        return False

    def check_score(self, player1, player2, screen_width, screen_height):
        if self.x <= 0:
            return player2

        if self.x >= screen_width - self.width:
            return player1

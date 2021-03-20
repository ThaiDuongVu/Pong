import pygame
import random
from direction import Direction


class Ball:
    # Initialize ball
    def __init__(self, direction, color, screen_width, screen_height):
        self.color = color

        self.width = 10
        self.height = 10

        self.x = screen_width / 2 - self.width / 2
        self.y = screen_height / 2 - self.height / 2

        self.max_speed = 5

        self.direction_horizontal = direction
        self.direction_vertical = Direction.Up

        if self.direction_horizontal == Direction.Left:
            self.speed_x = -self.max_speed
        elif self.direction_horizontal == Direction.Right:
            self.speed_x = self.max_speed
        else:
            self.speed_x = 0

        self.speed_y = 0

    # Draw ball on screen
    def draw(self, surface):
        pygame.draw.rect(surface, self.color, [
                         self.x, self.y, self.width, self.height])

        self.x += self.speed_x
        self.y += self.speed_y

    # Change direction of ball along the x axis
    def change_direction_horizontal(self):
        if self.direction_horizontal == Direction.Left:
            self.direction_horizontal = Direction.Right
            self.speed_x = self.max_speed

        elif self.direction_horizontal == Direction.Right:
            self.direction_horizontal = Direction.Left
            self.speed_x = -self.max_speed

        self.speed_y = random.uniform(-self.max_speed, self.max_speed)

    # Change direction of ball along the y axis
    def change_direction_vertical(self):
        if self.direction_vertical == Direction.Up:
            self.direction_vertical = Direction.Down

        elif self.direction_vertical == Direction.Down:
            self.direction_vertical = Direction.Up

        self.speed_y = -self.speed_y

    # Check whether ball is collided with player
    def check_collision_player(self, player):
        if player.x <= self.x <= player.x + player.width:
            if player.y <= self.y <= player.y + player.height:
                return True

        return False

    # Check whether ball is collided with wall
    def check_collision_wall(self, screen_height):
        if self.y <= 0 or self.y >= screen_height - self.height:
            return True

        return False
    
    # If ball goes out of bound, return which player will score
    def check_score(self, player1, player2, screen_width):
        if self.x <= 0:
            return player2

        if self.x >= screen_width - self.width:
            return player1

import pygame


class Separator:
    def __init__(self, color, screen_width):
        self.color = color

        self.width = 15
        self.height = 25

        self.x = screen_width / 2 - self.width / 2
        self.y = 0

    def draw(self, game_display, screen_height):
        for i in range(0, screen_height, self.height + 57):
            self.y = i
            pygame.draw.rect(game_display, self.color, [self.x, self.y, self.width, self.height])

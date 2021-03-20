import pygame


class Divider:
    # Initialize divider
    def __init__(self, color, screen_width):
        self.color = color

        self.width = 15
        self.height = 25

        self.x = screen_width / 2 - self.width / 2
        self.y = 0

    # Draw divider on screen
    def draw(self, surface, screen_height):
        for i in range(0, screen_height, self.height + 57):
            self.y = i
            pygame.draw.rect(surface, self.color, [
                             self.x, self.y, self.width, self.height])

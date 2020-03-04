import pygame


class Player:
    def __init__(self, player_id, color, screen_width, screen_height):
        self.color = color

        self.width = 10
        self.height = 60

        self.distance = 30
        self.player_id = player_id

        self.y = screen_height / 2 - self.height / 2
        if player_id == 1:
            self.x = self.distance
        elif player_id == 2:
            self.x = screen_width - self.distance - self.width

        self.speed = 0.5
        self.speed_y = 0

        self.score = 0

    def draw(self, game_display, screen_height):
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

    def get_score(self):
        return self.score

    def add_score(self):
        self.score += 1

    def get_id(self):
        return self.player_id

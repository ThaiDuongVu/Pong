import pygame


class Player:
    # Initialize player
    def __init__(self, id, color, screen_width, screen_height):
        self.color = color

        self.width = 10
        self.height = 60

        self.distance = 30
        self.id = id

        self.x = self.distance if id == 1 else screen_width - self.distance - self.width
        self.y = screen_height / 2 - self.height / 2

        self.max_speed = 8
        self.speed_y = 0

        self.score = 0

    # Draw player on screen
    def draw(self, surface, screen_height):
        pygame.draw.rect(surface, self.color, [
                         self.x, self.y, self.width, self.height])
        self.y += self.speed_y

        # Clamp player position to game bound
        if self.y < 0:
            self.y = 0
        if self.y > screen_height - self.height:
            self.y = screen_height - self.height

    # Move player up
    def move_up(self):
        self.speed_y = -self.max_speed

    # Move player down
    def move_down(self):
        self.speed_y = self.max_speed

    # Stop moving
    def stop(self):
        self.speed_y = 0

    # Return current player score
    def get_score(self):
        return self.score

    # Add score to current player
    def add_score(self):
        self.score += 1

    # Return player id
    def get_id(self):
        return self.id

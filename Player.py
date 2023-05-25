import pygame
from EnemySquare import EnemySquare

class Player:
    def __init__(self, colour, size):
        self.size = size
        self.colour = colour
        self.rect = pygame.Rect(0, 0, self.size, self.size)

    def draw(self, buffer):
        pygame.draw.rect(buffer, self.colour, self.rect)

    def move(self, buffer):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        x_centre = mouse_x
        y_centre = mouse_y
        self.rect.center = (x_centre, y_centre)
        self.draw(buffer)

import pygame
from EnemySquare import EnemySquare

class Player:
    def __init__(self, colour, size):
        self.size = size
        self.colour = colour
        self.xPos, self.yPos = pygame.mouse.get_pos()
        self.rect = pygame.Rect(self.xPos, self.yPos, self.size, self.size)

    def draw(self, buffer):
        pygame.draw.rect(buffer, self.colour, self.rect)

    def move(self, buffer):
        self.xPos, self.yPos = pygame.mouse.get_pos()
        self.rect = pygame.Rect(self.xPos, self.yPos, self.size, self.size)
        self.draw(buffer)

    def reset(self):
        self.rect.center = (self.size//2, self.size//2)

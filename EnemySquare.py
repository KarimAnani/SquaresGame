import pygame
import random
from pygame.locals import *

class EnemySquare:
    score = 0

    def __init__(self, buffer, colour, size, spawnSide, speed = 1):

        self.spawnSide = spawnSide
        self.size = size
        self.colour = colour
        self.speed = speed
        self.onScreen = False
        
        if self.spawnSide == 0: #left
            self.xPos = -10
            self.yPos = random.randint(0, buffer.get_height()-50)
            self.xDirection = random.randint(1, 10)
            self.yDirection = random.randint(-10, 10)
        elif self.spawnSide == 1: #right
            self.xPos = buffer.get_width()
            self.yPos = random.randint(0, buffer.get_height()-50)
            self.xDirection = random.randint(-10, -1)
            self.yDirection = random.randint(-10, 10)
        elif self.spawnSide == 2: #top
            self.xPos = random.randint(0, buffer.get_width()-50)
            self.yPos = -10
            self.xDirection = random.randint(-10, 10)
            self.yDirection = random.randint(1, 10)
        else: #bottom
            self.xPos = random.randint(0, buffer.get_width()-50)
            self.yPos = buffer.get_height()
            self.xDirection = random.randint(-10, 10)
            self.yDirection = random.randint(-10, -1)
        self.rect = pygame.Rect(self.xPos, self.yPos, self.size, self.size)

    def draw(self, buffer):
        pygame.draw.rect(buffer, self.colour, (self.xPos, self.yPos, self.size, self.size))


    def move(self, buffer):
        self.xPos += self.speed * self.xDirection
        self.yPos += self.speed * self.yDirection
        self.rect = pygame.Rect(self.xPos, self.yPos, self.size, self.size)

        if self.xPos < 0:
            self.xPos = 0
            self.xDirection *= -1
        elif self.xPos > buffer.get_width() - self.size:
            self.xPos = buffer.get_width() - self.size
            self.xDirection *= -1
        if self.yPos < 0:
            self.yPos = 0
            self.yDirection *= -1
        elif self.yPos > buffer.get_height() - self.size:
            self.yPos = buffer.get_height() - self.size
            self.yDirection *= -1

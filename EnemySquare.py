import pygame
import random
from pygame.locals import *

class EnemySquare:
    score = 0

    def __init__(self, buffer, colour, size, spawnSide):

        self.spawnSide = spawnSide
        self.size = size
        self.colour = colour
        self.onScreen = False

        '''
            There's a little hackiness to the way this works. I'm using "velocity" because it means direction and speed.
            The variable is doing two things:
            1. It's determining where the enemy square comes in from.
            2. It's determining direction.
            Once the EnemySquare is created, it's immediately drawn within the game's boundaries, where it bounces around.
            That way, I can avoid the issue of the game's boundaries preventing it from entering the screen in the first place.
        '''
        
        if self.spawnSide == 0: #left
            self.xPos = -10
            self.yPos = random.randint(0, buffer.get_height()-50)
            self.xVelocity = random.randint(1, 10)
            self.yVelocity = random.randint(-10, 10)
        elif self.spawnSide == 1: #right
            self.xPos = buffer.get_width()
            self.yPos = random.randint(0, buffer.get_height()-50)
            self.xVelocity = random.randint(-10, -1)
            self.yVelocity = random.randint(-10, 10)
        elif self.spawnSide == 2: #top
            self.xPos = random.randint(0, buffer.get_width()-50)
            self.yPos = -10
            self.xVelocity = random.randint(-10, 10)
            self.yVelocity = random.randint(1, 10)
        else: #bottom
            self.xPos = random.randint(0, buffer.get_width()-50)
            self.yPos = buffer.get_height()
            self.xVelocity = random.randint(-10, 10)
            self.yVelocity = random.randint(-10, -1)
        self.rect = pygame.Rect(self.xPos, self.yPos, self.size, self.size)

    def draw(self, buffer):
        pygame.draw.rect(buffer, self.colour, (self.xPos, self.yPos, self.size, self.size))


    def move(self, buffer):
        self.xPos += self.xVelocity
        self.yPos += self.yVelocity
        self.rect = pygame.Rect(self.xPos, self.yPos, self.size, self.size)

        if self.xPos < 0:
            self.xPos = 0
            self.xVelocity *= -1
        elif self.xPos > buffer.get_width() - self.size:
            self.xPos = buffer.get_width() - self.size
            self.xVelocity *= -1
        if self.yPos < 0:
            self.yPos = 0
            self.yVelocity *= -1
        elif self.yPos > buffer.get_height() - self.size:
            self.yPos = buffer.get_height() - self.size
            self.yVelocity *= -1

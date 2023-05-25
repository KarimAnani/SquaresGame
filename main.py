# Import our libraries
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1' # To remove the hello from the pygame community

import pygame
import random
import scores
import sys
from EnemySquare import EnemySquare
from Player import Player

pygame.init()

# Global screen variables. Could be too big. I think the game was more fun when it was cramped.
width = 800
height = 600

# Music
# Load and play  background music from any .wav files on the directory

music_choices = []

for filename in os.listdir(os.getcwd()):
    if filename.endswith('.wav'):  # Check if the file ends with '.wav'
        music_choices.append(filename)
        
songPlaying = random.randint(0, len(music_choices)-1)
pygame.mixer.music.load(music_choices[songPlaying])
pygame.mixer.music.play(-1)

# Prepare text stuff
textFont = pygame.font.Font(None, 64)

ready_text = textFont.render("Ready?", True, (0, 255, 0))
ready_rect = ready_text.get_rect(center=(width/2, height/2))

scoreFont = pygame.font.Font(None, 36)
endFont_text = pygame.font.Font(None, 30)
instructions_font = pygame.font.Font(None, 30)
instructions_text = instructions_font.render("Click anywhere. Avoid the green squares using the mouse.", 10,
                                             (0, 0, 0))
instructions_rect = instructions_text.get_rect(center=(width // 2, int(height * 0.6)))

# Set up the drawing window
captionsTuple = ("In the game of squares, you win or you die",
                 "These invading aliens are so square",
                 "Square yourself up to THESE babies",
                "They're gonna win fair and square",
            "Yee-haw! It's time to square up to some SQUARES",
                 "Three square meals in one square package",
                 "Avoid the green ones like they're responsibilities",
                 "Tactical Square Espionage Action"
                 )

caption = captionsTuple[random.randint(0, len(captionsTuple)-1)]
pygame.display.set_caption(caption)
screen = pygame.display.set_mode([width, height])

# Create an off-screen surface for speedy displays
buffer = pygame.Surface(screen.get_size())

# Start the game
def readyGame(buffer):
    waitForPlayerReady = True
    pygame.mouse.set_visible(True)
    while waitForPlayerReady:
        # Show the "Ready?" message
        buffer.fill((255, 255, 255))
        buffer.blit(ready_text, ready_rect)
        buffer.blit(instructions_text, instructions_rect)
        screen.blit(buffer, (0, 0))
        pygame.display.flip()

        # Wait for the player to click
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                waitForPlayerReady = False
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

# Game is actually running
def runGame(buffer):
    # Global (time)
    clock = pygame.time.Clock()
    FPS = 60
    timeSinceSpawn = 0
    milliseconds = 2000
    currentTime = pygame.time.get_ticks()
    lastTime = 0
    player = Player((255, 0, 0), 30)
    # Run until the user asks to quit
    gameIsRunning = True

    # For squares
    squares = []
    directions = (-1, 1)
    scores.resetScore()
    
    while gameIsRunning:
        # the buffer
        buffer.fill((255, 255, 255))

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameIsRunning = False
                pygame.quit()
                sys.exit()

        # Create EnemySquare Objects in-game

        if currentTime - timeSinceSpawn >= milliseconds:
            
            #speed = random.randint(1, 3
            spawnWhere = random.randint(0,3)
            # arguments = colour, size, spawnSide, speed = 1, 
            newSquare = EnemySquare(buffer, (0, 255, 0), 30, spawnWhere) # colour, size, spawn
            squares.append(newSquare)
            timeSinceSpawn = pygame.time.get_ticks()


        # Get the position of the mouse
        mouse_pos = pygame.mouse.get_pos()

        # Collision stuff

        for i in range(len(squares)):
            if player.rect.colliderect(squares[i].rect):
                gameIsRunning = False
                pygame.mixer.music.load('stop-sound.mp3')
                pygame.mixer.music.play(0)
                scores.checkHighScore()

                pygame.time.wait(2000)

                buffer.fill((255, 255, 255))
                            
                finalScore_text = textFont.render("Final Score: " + str(scores.gameScore), True, (0, 0, 0))
                thanks_text = endFont_text.render("Have another go!", True, (0, 0, 0))
                currentScore = int(scores.gameScore)
                scores.displayHighScore(buffer, currentScore)

                # Blitting final score and thanks
                # The high score is blitted in its own function
                # No, we won't change that
                
                buffer.blit(finalScore_text, finalScore_text.get_rect(center=(width//2, height//3)))
                buffer.blit(thanks_text, thanks_text.get_rect(center=(width//2, int(height*0.6))))

                # Blit the updated buffer
                screen.blit(buffer, screen.get_rect(center=(width, height)))
                pygame.display.flip()

                songPlaying = random.randint(0, len(music_choices)-1)
                pygame.mixer.music.load(music_choices[songPlaying])
                pygame.mixer.music.play(-1)
                break # I think I fixed it by breaking out of the inner loop
                
            else:
                # Actually move the player
                squares[i].move(buffer)
                squares[i].draw(buffer)
                player.move(buffer)

                # I was accindetally calling draw() twice there.
                # player.draw(buffer)
        
        pygame.mouse.set_visible(False)
        currentTime = pygame.time.get_ticks()
        if currentTime - lastTime >= 1000:
            scores.updateScore()
            lastTime = currentTime

        # Display score so far
        if gameIsRunning:
            score_text = scoreFont.render(f"Score: {scores.gameScore}", True, (0, 0, 0))
            buffer.blit(score_text, (10, 10))

        # NEVER DELETE
        screen.blit(buffer, (0, 0))  
        pygame.display.flip()
        clock.tick(FPS)

while True:
    readyGame(buffer)
    runGame(buffer)
    #pygame.time.wait(3000)
    pauseTime = pygame.time.get_ticks()
    while True:
        presently = pygame.time.get_ticks()
        if presently - pauseTime > 3000:
            break
# Done! Next line is redundant, but just in case
pygame.quit()

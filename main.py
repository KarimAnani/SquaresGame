# Import and initialize the pygame library
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1' # To remove the hello from the pygame community

import pygame
import random
import scores
from EnemySquare import EnemySquare
from Player import Player
pygame.init()

# Global variables
width = 800
height = 600

# Global (time)
clock = pygame.time.Clock()
FPS = 60
timeSinceSpawn = 0
milliseconds = 2000
currentTime = pygame.time.get_ticks()
lastTime = 0

# Music
# Load and play the background music
music_choices = ('Arabian_Salsa_1.wav',
                 'Grease_Monkey.wav',
                 'Happy_1.wav')
songPlaying = random.randint(0, len(music_choices)-1)
pygame.mixer.music.load(music_choices[songPlaying])
pygame.mixer.music.play(-1)

# Text
textFont = pygame.font.Font(None, 64)

ready_text = textFont.render("Ready?", True, (0, 255, 0))
ready_rect = ready_text.get_rect(center=(width/2, height/2))
scoreFont = pygame.font.Font(None, 36)

endFont_text = pygame.font.Font(None, 30)
instructions_font = pygame.font.Font(None, 30)
instructions_text = instructions_font.render("Avoid the green squares using the mouse for as long as you can.", 10,
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
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption(caption)

# Create an off-screen surface
buffer = pygame.Surface(screen.get_size())

# Run until the user asks to quit
gameIsRunning = True

# For squares
squares = []
directions = (-1, 1)

# Player class takes(colour, size, array)
player = Player((255, 0, 0), 30)

# Other functions
def setup_game():
    # Create the player object
    player = Player(300, 200)

    # Create the EnemySquare objects
    squares = []
    time_since_spawn = pygame.time.get_ticks()
    milliseconds = 10000000
    return player, squares, time_since_spawn, milliseconds

# Start the game

waitForPlayerReady = True
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

# Game is actually running

while gameIsRunning:
    # the buffer
    buffer.fill((255, 255, 255))

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameIsRunning = False

    # Create EnemySquare Objects in-game

    if pygame.time.get_ticks() - timeSinceSpawn >= milliseconds:
        
        #speed = random.randint(1, 3)
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
            thanks_text = endFont_text.render("Thanks for playing!", True, (0, 0, 0))
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

            pygame.mixer.music.load(music_choices[songPlaying])
            pygame.mixer.music.play(-1)
            break # I think I fixed it by breaking out of the inner loop
            
        else:
            # Actually move the player
            squares[i].move(buffer)
            squares[i].draw(buffer)
            player.move(buffer)
            player.draw(buffer)
    
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


pygame.time.wait(3000)

# Done!

pygame.quit()

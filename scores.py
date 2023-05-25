# This will handle all the score stuff

import os
import pygame

gameScore = 0

def resetScore():
    global gameScore
    gameScore = 0

def updateScore():
    global gameScore
    gameScore += 1
    return gameScore

def checkHighScore():
    global gameScore
    high_score_file = 'high_score.txt'

    try:
        if os.path.isfile(high_score_file):
            with open(high_score_file, 'r') as file:
                contents = file.readlines()

                last_highscore = int(contents[0].split(':')[1].strip())
                current_highscore = int(contents[1].split(':')[1].strip())

                if gameScore > current_highscore:
                    last_highscore, current_highscore = current_highscore, gameScore

                    with open(high_score_file, 'w') as file:
                        file.write(f"last_score: {last_highscore}\n")
                        file.write(f"new_score: {current_highscore}")
        else:
            with open(high_score_file, 'w') as file:
                file.write(f"last_score: 0\n")
                file.write(f"new_score: {gameScore}")
    except FileNotFoundError:
        with open(high_score_file, 'w') as file:
            file.write(f"last_score: 0\n")
            file.write(f"new_score: {gameScore}")



def displayHighScore(screen, score):
    # Open the high score file in read mode
    with open('high_score.txt', 'r') as file:
        # Read the contents of the file
        contents = file.readlines()
        # Extract the last score and new score from the file contents
        highscore = int(contents[1].split(':')[1].strip())
        
        # Render the high score text on the screen

        font = pygame.font.Font(None, 36)

        if gameScore == highscore:
            # This checks if they're equal because the high score's already updated in checkHighScore()
            # El oh el
            highscore_text = font.render(f"Ding ding ding! There's a new champion! Score: {score}", True, (0, 0, 255))
        else:
            highscore_text = font.render(f"The old high score, {highscore}, remains undisputed!", True, (0, 0, 255))

        # Calculate the position to display the scores on the screen
        text_x = screen.get_width() // 2 - highscore_text.get_width() // 2
        text_y = screen.get_height() // 2 - highscore_text.get_height() // 2
        screen.blit(highscore_text, (text_x, text_y))

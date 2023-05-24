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
    try:
        # Check if the file exists
        if os.path.isfile('high_score.txt'):
            # Open the high score file in read mode
            with open('high_score.txt', 'r') as file:
                # Read the contents of the file
                contents = file.readlines()

                # Extract the last score from the file contents
                last_highscore = int(contents[0].split(':')[1].strip())
                current_highscore = int(contents[1].split(':')[1].strip())

                if gameScore > current_highscore:
                    last_highscore = current_highscore
                    current_highscore = gameScore

                    # Open the high score file in write mode
                    with open('high_score.txt', 'w') as file:
                        # Write the new high score and old high score to the file
                        file.write(f"last_score: {last_highscore}\n")
                        file.write(f"new_score: {current_highscore}")
        else:
            # If the file doesn't exist, create it and set the new high score
            with open('high_score.txt', 'w') as file:
                file.write(f"last_score: 0\n")
                file.write(f"new_score: {gameScore}")
    except FileNotFoundError:
        # Set the old high score to 0
        old_high_score = 0

        # Create the high score file and set the new high score
        with open('high_score.txt', 'w') as file:
            file.write(f"last_score: {old_high_score}\n")
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
            # Because it's already updated
            # Could also write score == lastscore
            # Should have been updating the score and all in THIS function
            # El oh el
            highscore_text = font.render(f"Ding ding ding! There's a new champion! Score: {score}", True, (0, 0, 255))
        else:
            highscore_text = font.render(f"The old high score, {highscore}, remains undisputed!", True, (0, 0, 255))

        # Calculate the position to display the scores on the screen
        text_x = screen.get_width() // 2 - highscore_text.get_width() // 2
        text_y = screen.get_height() // 2 - highscore_text.get_height() // 2
        screen.blit(highscore_text, (text_x, text_y))

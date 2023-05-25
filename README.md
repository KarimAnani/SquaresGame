# Readme
## Background
I decided to code something, start to finish, in a few hours, since I suddenly had downtime and hadn't programmed anything in about a decade; I couldn't even remember how to  write a for loop. This game (imaginatively titled _Squares_) was the result. Short of a main menu, the ability to restart the game, and type in who's just scored, I succeeded. I hope it's fun.

## How to play
Just run the file main.py. Avoid the green squares for as long as you can. If you get bored, exit by pressing close.

## Heads-up: Text file will be saved on your device
The game will create a text file when it runs to store a high score. On the one hand, it's a bit of a make-do solution; I need to learn how to properly store data. On the other, you can restart the high score by deleting the file—or even change it to impress your friends. What this game lacks in programming integrity, it makes up for in relationship-building potential. Maybe even romance. Turn heads. Give yourself a high score of 1,000,000 today.

## Music
The music was taken from [Royalty Free Music Clips](https://www.royaltyfreemusicclips.com/pir/free_music_loops.shtml). I'm _trusting_ it's royalty-free. In the current build, the game checks if there are .wav files, then slaps a list together out of them to play. If you want to add music to the game, just throw it in the dist folder, although if it's mp3, move it into a separate directory and adjust the code accordingly to avoid playing the stop sound for music. Or play the stop sound for music. Who am I to judge?

## Probably embarrassing things
- Naming conventions are a hodgepodge; there's a mixture of camel case and underscores. I was typing furiously and testing, only refactoring code once or twice throughout to make fixes easier.
- Attempting to move the main loop into a different file with more manageable function calls added a two-second delay to starting the game. Not sure if there's a fix for that or if that slowness comes with Python. I had to move it back to the main file to keep it smooth.
- As a consequence, the main file is long. But, I hope, self-documenting and readable. I’ve thrown in comments.

# Licence
Obviously, this game works off of Pygame. [They have their licence](https://github.com/pygame/pygame#license), which at the time of writing is GNU LGPL version 2.1. For the original code, I'm happy for anyone to fork/improve upon/add to. All I ask is you link here and/or don't throw my code into a closed system. It's not exactly John Carmack-level work, but I appreciate any love I was denied in my childhood.

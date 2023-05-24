# Readme
## Background
I wanted to code something in a few hours, since I had sudden downtime and hadn't coded anything except some personal work tools in about a decade (I couldn't even remember how to loop!), and this game (imaginatively titled "Squares") was the result. My goal was to make something from start to finish. Short of a main menu, including the ability to restart the game, I succeeded. I hope it's fun.

## How it's Played
Just run the main file. Simple. Avoid the green squares as long as you can. If you get bored, you can by pressing X at any point.

## Heads-Up: Text file will be saved on your device
The game will create a text file when it runs to store a high score. Obviously, bit of a make-do solution, and I need to read-up on how to properly do that. But, yeah, if you want to restart the high score (or change it completely to impress anyone that you've scored a million or something), it's a .txt file.

## Music
The music was taken from [Royalty Free Music Clips](https://www.royaltyfreemusicclips.com/pir/free_music_loops.shtml) and is ostensibly royalty-free.

## Probably embarrasing things
- Naming conventions are a hopgepodge; there's a mixture of camel case and underscores. I was typing furiously and testing, only refactoring code once or twice throughout to make fixes easier.
- Attempting to move the main loop into a different file with more manageable function calls added a two-second delay to starting the game. Not sure if there's a fix for that or if that slowness comes with Python. I had to move it back to the main file to keep it smooth.
- As a consequences, the main file is a lot of spaghetti. But, I hope, self-documenting and readable.

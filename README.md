# CS50 final project: Minesweeper


## Game description

Minesweeper is a classic puzzle game that was popular with Microsoft's older Windows operating-system. It's a grid-based game in which a player has to open the tiles one by one by clicking on them. There are different kinds of tiles i.e. empty tiles, numbered tiles, mines. Initially, all the tiles are hidden. To win this game player has to open all the tiles that are not mine by clicking on them. If a player accidentally clicks a tile that is mine then the game is over. There is an additional feature of a flag which is toggled by right-clicking on a tile. If a tile is flagged, then it can't be open until the flag is turned off by right-clicking on a flagged tile. This particular feature is mostly used to flag the tiles that are supposedly mined, to prevent them from detonating accidentally.

In this project, the entry point is `main.py` and there are different classes and functions written for games. For texts and images, there are separate folders. The grid and tile for the game play, texts, and buttons for the interactions have their own classes written in their own separate files. The constants of the game which are used throughout the game are in a separate file. The core of the game is in play.py file, in which there are different stages, i.e. base state, game loop, and game-over state. There are several helper functions written which capture what the player is doing and update the game window or show messages accordingly.


## Getting Started

The entire project is developed using `python` language. `Pygame` module is used to develop this game. Hence it's required to be installed on your computer to play this game.


## Required Tools

* Python version 3.6, pip, and setuptools
* Pygame module version 1.96


## How to play

1. Clone or download this project. 
2. Go to the minesweeper directory. Run the `main.py` file to play the game. You can also do with the command `python3 main.py` at your terminal.
3. If there is an `import error`, in case that you don't already have `pygame` installed. Run `pip install -r requirement.txt` command to install rquired module.
4. Repeat step-2.


## TODOs

* Make the game more interactive with user-given grid size and number of mines.
* Some sound effects and background music for the game.
* Add a high score (best time) feature and display top players after the game is won/lost.
* Remove redundancy if any, optimize imports


## Built Using

 [Pycharm](https://www.jetbrains.com/pycharm/download/#section=windows) - The IDE that is used to develop the game


## Acknowledgments

* About game: https://en.wikipedia.org/wiki/Minesweeper_(video_game)

* Inspirations:
  1. David J. Malan, the Harvard professor who teaches cs50 (one of the many courses).
  2. Colton Ogden, the cs50 staff who live-streamed this game development on [Twitch](https://www.twitch.tv/cs50tv) using `Lua` language, he also taught [game-dev](https://cs50.harvard.edu/games/) course at Harvard.
  3. CS50's and MIT's CS staff who helped me learn python, adapt a good coding style, and how to solve problems using good algorithms.


## Suggestions

Any suggestions and/or optimizations to make the game better are most welcome!

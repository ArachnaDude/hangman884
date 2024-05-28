# Hangman

A silent crowd gathers around the gallows, as a deadly game of life and death plays out, where every wrong step tightens the noose. Can you guess the solution, or will you send an innocent victim to their fate?

## Description

Hangman is a classic pen-and-paper game in which one player thinks of a word or phrase, and the other player(s) guess letters to try and decode it.

This project implements an object-oriented version of the game, where the computer selects a hidden puzzle, and the player attempts to guess it. The game starts with a preset number of lives (default 5). Guessing a letter correctly adds it to the solution but each incorrect guess loses you a life. If you run out of lives, it's game over!
The learning goals for the project are:

- To use object-oriented programming techniques
- To better understand control flow within the scope of the project
- To be able to improve on the basic spec of the project

## Installation

In your terminal:

```
$ git clone https://github.com/ArachnaDude/hangman884.git
$ cd hangman884
```

Open up your text editor of choice to view and run the files. The game does not utilise any packages that require separate installation.

## Usage

The logic of asking for and validating user input is controlled by the `Hangman()` class defined in `milestone_5.py`.
However the user will interact with the game through the `play_game()` function in the same file.

Players guess a single letter, by typing it on the keyboard and then pressing enter. If the player tries to guess a non-letter character, or more than one character, the game will deny the input, and request a new input from the player.

Under normal usage, the game will run until the player either wins or loses. However `ctrl + C` on the keyboard will end the program, and lose any progress the player has made.

To make the game either easier or harder, change the `num_lives` variable in the `play_game()` function, decreasing the number for an additional challenge, or increasing it to reduce the difficulty.

For detailed instructions on the methods in the Hangman class, or for playing the game, type `help(Hangman)`, or `help(play_game)` in your terminal.

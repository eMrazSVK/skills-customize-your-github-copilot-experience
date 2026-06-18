# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman game in Python to practice loops, conditionals, and string manipulation. By completing this assignment, you will learn how to manage game state and user input in an interactive terminal program.

## 📝 Tasks

### 🛠️	Set Up the Game Structure

#### Description
Create the core setup for the Hangman game. Define a small list of words, choose one word at random, and initialize the variables needed to track guessed letters and remaining attempts.

#### Requirements
Completed program should:

- Define a predefined list of possible words.
- Randomly select one word from the list at the start of the game.
- Initialize a display format for the hidden word (for example: `_ _ _ _`).
- Initialize a counter for incorrect guesses remaining.


### 🛠️	Implement Gameplay Loop

#### Description
Build the main game loop that asks the player for letter guesses, updates progress, and checks win or loss conditions after each guess.

#### Requirements
Completed program should:

- Accept one letter guess at a time from the player.
- Reveal correctly guessed letters in their correct positions.
- Decrease remaining attempts only for incorrect guesses.
- End with a clear win message when the word is fully guessed.
- End with a clear loss message when attempts are exhausted.

# Vocabulary Flashcards Game

A simple and educational flashcard-style game to help players improve their English vocabulary.

## Game Description

This game helps players improve their English vocabulary through a memory-matching game. Players are shown English words along with their definitions or synonyms as flashcard pairs. After a brief period to memorize the pairs, all cards are flipped and shuffled, and the player must match each word with its correct definition by selecting two cards at a time.

## Features

- Retro pixel-style graphics for a clean and nostalgic look
- Timer to track how long it takes to complete the matches
- Scoring system based on accuracy and speed
- Multiple difficulty levels (4, 8, or 12 pairs)
- Sound effects for correct/incorrect matches
- Themed vocabulary sets (General, Business, Science, Travel)
- Review mode to revisit pairs that were matched incorrectly

## Requirements

- Python 3.6 or higher
- Pygame library

## Installation

1. Make sure you have Python installed on your system
2. Install Pygame:
   ```
   pip install pygame
   ```
3. Clone or download this repository
4. Add sound files to the `assets/sounds` directory (see README in that folder)

## How to Play

1. Run the game:
   ```
   python main.py
   ```
2. Select a difficulty level and vocabulary set from the menu
3. Click "Start Game" to begin
4. Memorize the word-definition pairs shown on the cards
5. After the cards are flipped, click on two cards to try to match a word with its definition
6. Match all pairs to complete the game
7. Review any incorrect matches in the review mode

## Game Controls

- Mouse: Click on cards to flip them and navigate menus
- ESC key: Quit the game

## Scoring

- +10 points for each correct match
- -2 points for each incorrect match (minimum score is 0)

## Adding Custom Vocabulary Sets

You can add your own vocabulary sets by editing the `data/vocabulary.py` file. Follow the existing format to add new word-definition pairs.

## License

This project is open source and available for educational purposes.

## Credits

Created as an educational project to help improve English vocabulary skills.

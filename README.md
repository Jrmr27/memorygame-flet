# Memory Game with Flet
A memory card game built with Flet framework in Python, featuring car matching mechanics, score tracking and multiple game states. In this game, player needs to match pairs of cards while keeping track of the matches and errors made during the game.

## Project Structure
memorygame/
└── base/
└── src/
├── assets/
│ └── images/
│ ├── cover.png
│ ├── congrats.png
│ └── [0-19].png
├── views/
│ ├── home.py
│ ├── card.py
│ ├── game.py
│ └── congrats.py
└── main.py

## Requisites
- Python 3.x
- Framework Flet

## Instal
pip install flet

## How to Execute 
1st -> go to the directory of the project on the terminal
cd memorygame
cd base
cd src
2nd -> execute the main.py to start the game 
flet run -d main.py

## Characteristics
- Interactive memory game with 10 pairs of cards
- Counter of matches and errors
- Animation when flipping the cards
- Multiple game states with navegation

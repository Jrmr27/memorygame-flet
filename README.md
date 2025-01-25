# Memory Game with Flet
A memory card game built with Flet framework in Python. Features include card matching mechanics, score tracking, animated card flips, and multiple game states. Players must find matching pairs while keeping track of their matches and errors.


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
- Flet Framework

## Install
pip install flet

## How to Run
1st -> go to the directory of the project on the terminal
cd memorygame
cd base
cd src
2nd -> run the main.py to start the game 
flet run -d main.py

## Characteristics
- Interactive memory game with 10 pairs of cards
- Counter of matches and errors
- Animation when flipping the cards
- Multiple game states with navegation

# Memory Game (Jogo da Memória)


A classic **Memory Game** implemented in Python using the `tkinter` library for the graphical interface and `Pillow` (PIL) for image processing. The game features three difficulty levels, dynamic board generation, and a persistent high-score tracking system.

---

## Table of Contents
1. [Features](#features)
2. [Tech Stack](#tech-stack)
3. [Quick Start](#quick-start)
4. [Repository Structure](#repository-structure)
5. [How It Works & Usage](#how-it-works--usage)
6. [Game Mechanics](#game-mechanics)
7. [Data Structures](#data-structures)
8. [License](#license)

---

## Features

- **Interactive GUI**: Built entirely with Python's native Tkinter library for a seamless desktop experience.
- **Dynamic Board Generation**: Shuffles the deck automatically on every new game, ensuring a unique layout every time.
- **Three Difficulty Levels**: Scales the grid size and number of pairs to match your skill level.
- **Highscore Tracking**: Saves your best score (fewest moves to win) for each difficulty level locally.
- **Visual Feedback**: Cards reveal themselves smoothly with a 1-second delay upon a mismatch to allow the player to memorize the positions.

---

## Tech Stack

- **Language:** Python 3
- **GUI Framework:** Tkinter (Native Python)
- **Image Processing:** Pillow (`PIL`)
- **Data Persistence:** Local Data File (Native Python)

---

## Quick Start

### Prerequisites
Make sure you have Python installed along with the Pillow library for image processing.

```bash
pip install Pillow
```

### Build & Run
1. Clone the repository:
```bash
git clone https://github.com/Difath/memory-game-python.git
cd memory-game-python
```

2. Run the game:
```bash
python memory_game.py
```

3. To reset the highscores at any time, run:
```bash
python reset_highscore.py
```

---

## Repository Structure

```bash
/.
├── memory_game.py       # Main game script (GUI, logic, and loops)
├── reset_highscore.py   # Utility script to wipe saved highscores
├── numeros/             # Directory containing card face assets (1.png to 40.png)
│   └── semFace.png      # Asset for the back of the card
├── highscore/           # Directory where local highscores are saved
├── .gitignore           # Git ignore rules
├── LICENSE              # MIT License
└── README.md            # Project documentation
```

---

## How It Works & Usage

When you launch the game, you are greeted with a main menu where you must select a difficulty level.

### Difficulty Levels

| Difficulty | Grid Size | Total Cards | Total Pairs | Description |
|------------|-----------|-------------|-------------|-------------|
| **Fácil (Easy)** | 6 x 4 | 24 | 12 | Perfect for beginners or a quick warmup. |
| **Médio (Medium)** | 8 x 4 | 32 | 16 | A balanced challenge that tests your short-term memory. |
| **Difícil (Hard)** | 10 x 4 | 40 | 20 | The ultimate memory test using almost the entire deck. |

Once a difficulty is selected, the grid is rendered instantly, and the game begins. Your current move count and the absolute highscore for that difficulty are displayed at the bottom of the screen.

---

## Game Mechanics

1. **Flipping Cards:** 
   - Click any card showing the `semFace.png` back cover to flip it over.
   - The image is loaded from the `numeros/` folder dynamically.
2. **Matching:**
   - **Match:** If the second card matches the first, both remain face-up permanently for the rest of the game.
   - **Mismatch:** If they do not match, the game pauses interactions for exactly **1 second**. This delay is crucial as it gives the player time to memorize the positions of the two cards before they automatically flip back face-down.
3. **Move Counting:** Every time you flip a pair (whether a match or a mismatch), your "Nº de Jogadas" (Number of Moves) increments by 1.
4. **Victory Condition:** Match all pairs on the board to win. If your total move count is lower than the saved highscore, the game overwrites the highscore with your new record.

---

## Data Structures

The game relies on an Object-Oriented approach for card management:

### The `Carta` Class
Every card on the board is an instance of the `Carta` class, which holds its state and metadata:
- `Tkimage`: The Pillow image object loaded into Tkinter.
- `numero`: The ID of the card (used to verify matches).
- `estado`: A string representing the card's visibility (`"escondido"` or `"visivel"`).
- `esta_feito`: A boolean that locks the card permanently face-up once a match is found (`True`).

### Global State Management
- `baralho`: A list containing all `Carta` objects currently in play.
- `primeira_carta_do_par` & `segunda_carta_do_par`: Arrays holding the index, number, and Tkinter widget reference of the currently selected cards to allow comparison and resetting.
- `jogo_a_funcionar`: A boolean lock that prevents the user from clicking a 3rd card while the 1-second mismatch delay is happening.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

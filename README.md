# Memory Game (Jogo da Memória)

![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

A classic **Memory Game** implemented in Python using the `tkinter` library for the graphical interface and `Pillow` (PIL) for image processing. The game features three difficulty levels, dynamic board generation, and a persistent high-score tracking system.

## 📌 Features

- **Interactive GUI**: Built entirely with Python's native Tkinter library.
- **Three Difficulty Levels**:
  - **Easy (Fácil)**: 6x4 Grid (12 pairs)
  - **Medium (Médio)**: 8x4 Grid (16 pairs)
  - **Hard (Difícil)**: 10x4 Grid (20 pairs)
- **Highscore Tracking**: Saves your best score (fewest moves to win) for each difficulty level locally using the Python `shelve` module.
- **Visual Feedback**: Cards reveal themselves smoothly with a 1-second delay upon a mismatch to allow the player to memorize the positions.
- **Dynamic Board**: Shuffles the deck automatically on every new game.

## 🛠️ Tech Stack

- **Language:** Python 3
- **GUI Framework:** Tkinter (Native Python)
- **Image Processing:** Pillow (`PIL`)
- **Data Persistence:** `shelve` (Native Python)

## 🚀 Quick Start

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

## 📁 Repository Structure

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

## 🎮 How It Works

1. **Start Screen:** You are presented with a main menu to select the difficulty.
2. **Gameplay:** The board is drawn based on the selected difficulty. Click a card to reveal its face.
3. **Matching:**
   - If the second card matches the first, they remain face-up.
   - If they do not match, a 1-second delay occurs before they flip back face-down, allowing you to memorize them.
4. **Winning:** Match all pairs to win the game. Your score is based on the total number of moves (pairs flipped). If your score beats the local highscore, it will be saved!

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

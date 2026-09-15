# Letter & Number Attention Game

A desktop-based interactive attention and reaction-time game developed in Python using Tkinter.

The application presents the player with a randomly generated letter and number. For each round, the player is instructed to classify either the **letter** or the **number** using two response buttons: **Left** and **Right**.

## Game Rules

### Letter Classification
- **Left** → Vowel
- **Right** → Consonant

### Number Classification
- **Left** → Even number
- **Right** → Odd number

The order of the displayed letter and number is randomized in each round, while the required classification target changes between `LETTER` and `NUMBER`.

## How the Game Works

Each game consists of 30 rounds.

For every round:

1. A random letter from `A-Z` is generated.
2. A random number from `1-9` is generated.
3. The program randomly selects either `LETTER` or `NUMBER` as the classification target.
4. The letter and number are displayed in random order.
5. The player selects **Left** or **Right**.
6. The program checks whether the answer is correct.
7. The player's response time is measured.
8. The score and reaction-time data are recorded.

At the end of the game, the application reports the player's overall accuracy and response-time statistics.

## Features

- Graphical user interface built with Tkinter
- Random letter and number generation
- Randomized classification tasks
- Left/Right button-based interaction
- 30-round gameplay
- Accuracy tracking
- Reaction-time measurement for every round
- Average response time calculation
- Fastest and slowest response calculation
- Detailed per-question response-time report
- Replay functionality

## Technologies Used

- Python
- Tkinter
- `random` module
- `time.perf_counter()` for reaction-time measurement

## Reaction-Time Measurement

The timer starts when a new question is displayed:

```python
self.answer_start_time = time.perf_counter()
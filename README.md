# Rock-Paper-Scissors Game

## Overview

This project consists of a simple console-based Rock-Paper-Scissors game implemented in Python. Players can choose to compete against a robot (PvE) or another player (PvP). The game allows multiple rounds and provides feedback on the results of each match.

## Files

- `pve.py`: Contains the logic for Player vs. Environment mode.
- `pvp.py`: Contains the logic for Player vs. Player mode.
- `main.py`: The main entry point that allows the user to select between PvE and PvP modes.

## Getting Started

### Prerequisites

Make sure you have Python 3.x installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Running the Game

1. Clone or download the repository to your local machine.
   ```bash
   git clone https://github.com/AndrewAMur/Roshambo.git
   cd Roshambo
   ```

2. Run the main game script:
   ```bash
   python main.py
   ```

3. Follow the on-screen prompts to choose between PvP and PvE modes.

### Gameplay

- In **PvE mode**, you will play against a robot. You will choose Rock, Paper, or Scissors, and the robot will randomly select one as well. The outcome of the match will be displayed.
- In **PvP mode**, two players will take turns selecting their choices. The game will then determine the winner based on the rules of Rock-Paper-Scissors.
- After each game, you will have the option to play again or exit.

### Game Rules

- Rock crushes Scissors
- Scissors cuts Paper
- Paper covers Rock
- If both players choose the same option, the game is a tie.

## Code Structure

- **pve.py**
  - Defines the robot's choice and handles the user's input.
  - Implements the logic to determine the winner between the user and the robot.

- **pvp.py**
  - Allows two players to input their choices and determines the winner.

- **main.py**
  - Acts as the entry point for the game, allowing the user to choose between PvP and PvE modes.
  - Manages the overall game loop and prompts for replaying the game.

## Contributing

Feel free to fork the repository and make improvements or report issues. Pull requests are welcome!

## License

This project is open-source and available under the [MIT License](LICENSE).

## Acknowledgements

Thanks to the contributors of Python's standard libraries, which made implementing this game straightforward and enjoyable!

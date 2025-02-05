# How to Play "Hidden Maze Runner"
Run 'python maze.py' in the terminal when in maze_runner_ai repository.

# Main Menu Page
1. Escape
   - Click on "Escape" to go to the level selection screen.
2. Instructions
   - Click on "Instructions" to view an overview of the game mechanics and objectives.

# Level Selection
1. Easy
   - Select this to play an 5x6 grid maze.
2. Medium
   - Select this to play an 11x10 grid maze.
3. Hard
   - Select this to play a 15x14 grid maze.
4. God Mode
   - Select this to play a 18x20 grid maze.
5. Custom
   - Select this to play a custom maze. Note: You can edit the custom map directly in the code using VS Code.

Each level selection screen includes a Back button to return to the main menu.

# Starting the Game
- After selecting a level, all players (the human player and three AI opponents) start at the same point.
- The human player moves first, followed by the AI players in sequence.

# Player Navigation
- Mouse: Click on the path to move your character to the desired location.

# AI Opponents
- Compete against AI players, each using a different search algorithm:
  - A\* Search: Efficiently finds the shortest path by balancing actual travel cost and heuristic estimates.
  - Breadth-First Search (BFS): Systematically explores all possible paths, ensuring the shortest path in terms of steps.
  - Depth-First Search (DFS): Explores paths deeply before backtracking, suitable for mazes with deep, singular paths.

# Power-ups
While travelling along a path, you may encounter some power-ups:
- Blue Power-up: Teleports you to the shortest path leading directly to the finish line.
- Red Power-up: Randomly teleports you to a different location on the map, which could be advantageous or detrimental.
- Purple Power-up: Reveals the entire maze layout for 1 second, allowing you to plan your path. During this time, AI players can advance by one move.

# Winning or Losing
- Win Screen
  - If you reach the finish line first, a congratulatory message will be displayed.
  - Click the button to return to the main menu.
- Lose Screen
  - If an AI player reaches the finish line first, a message indicating you lost will be displayed.
  - Click the button to return to the main menu.

# Custom Map
- Editing: Edit the custom map in the code using VS Code.
- Playing: Start the game with all players at the same starting line and navigate the maze by clicking with the mouse.

By following these instructions, you can fully engage with "Hidden Maze Runner," enjoy the competitive and strategic gameplay, and explore the practical applications of AI search algorithms in a gaming context.

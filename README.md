# Pathfinding with A* Algorithm

## Overview
This project implements the A* (A-star) pathfinding algorithm to find the shortest path between a start and goal point in a grid-based environment. The A* algorithm combines the benefits of Dijkstra's Algorithm and Greedy Best-First Search by using a heuristic function to optimize the search process.

## Features
-  Visual representation of the grid
-  Interactive start and goal selection
-  Obstacle placement
- Real-time pathfinding updates
- Adjustable grid size and heuristic function

## How A* Works
A* uses the following cost function to determine the best path:

```math
f(n) = g(n) + h(n)
```

where:
- `g(n)`: The actual cost from the start node to node `n`
- `h(n)`: The estimated cost from node `n` to the goal (heuristic function)

## Usage
### 1. Clone the repository
```sh
git clone https://github.com/yourusername/pathfinding-a-star.git
cd pathfinding-a-star
```

### 2. Install dependencies (if applicable)
#### For Python projects:
```sh
pip install -r requirements.txt
```

### 3. Run the application
#### For Python:
```sh
python main.py
```
### 4. Interact with the UI to set the start and goal nodes and visualize the path.

## Dependencies
### Python:
- `pygame`
- `numpy`

## Customization
- Modify the heuristic function in `astar.py` (for Python).
- Adjust grid size in the configuration file.
- Add different types of obstacles or weighted paths for advanced pathfinding.




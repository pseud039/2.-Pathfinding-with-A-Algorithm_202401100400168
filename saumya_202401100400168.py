# -*- coding: utf-8 -*-
"""Saumya_202401100400168.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1nO8SAsgcxU2VCLvQ-KMCKwQXA3GwKWob
"""

import heapq  # Importing heap queue for priority queue operations

class Node:
    """Class representing a node in the A* algorithm."""

    def __init__(self, position, parent=None):
        """
        Initializes a node.
        :param position: Tuple (x, y) representing node coordinates.
        :param parent: Reference to parent node (used to reconstruct the path).
        """
        self.position = position  # Node's position (x, y)
        self.parent = parent  # Pointer to parent node for path reconstruction
        self.g = 0  # Cost from start node to this node
        self.h = 0  # Estimated cost from this node to goal (heuristic)
        self.f = 0  # Total cost (g + h)

    def __lt__(self, other):
        """Defines priority comparison for heapq (lower f-value is preferred)."""
        return self.f < other.f

def astar(grid, start, goal):
    """
    Implements A* algorithm for pathfinding.
    :param grid: 2D list representing the map (0 = walkable, 1 = obstacle).
    :param start: Tuple (x, y) representing start position.
    :param goal: Tuple (x, y) representing goal position.
    :return: List of tuples representing the shortest path.
    """

    # Priority queue (min-heap) to store open nodes
    open_list = []
    closed_set = set()  # Set to store visited nodes

    # Initialize start and goal nodes
    start_node = Node(start)
    goal_node = Node(goal)

    # Push start node into the open list
    heapq.heappush(open_list, start_node)

    while open_list:
        # Get the node with the lowest f-value from the priority queue
        current_node = heapq.heappop(open_list)
        closed_set.add(current_node.position)  # Mark node as visited

        # If we reached the goal, reconstruct and return the path
        if current_node.position == goal:
            path = []
            while current_node:
                path.append(current_node.position)  # Backtrack from goal to start
                current_node = current_node.parent
            return path[::-1]  # Reverse the path to get correct order

        # Define movement directions (Up, Down, Left, Right)
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for dx, dy in neighbors:
            neighbor_pos = (current_node.position[0] + dx, current_node.position[1] + dy)

            # Check if neighbor is within grid bounds and walkable
            if (0 <= neighbor_pos[0] < len(grid) and
                0 <= neighbor_pos[1] < len(grid[0]) and
                grid[neighbor_pos[0]][neighbor_pos[1]] == 0 and
                neighbor_pos not in closed_set):

                # Create neighbor node
                neighbor_node = Node(neighbor_pos, current_node)
                neighbor_node.g = current_node.g + 1  # Cost from start node
                neighbor_node.h = abs(neighbor_pos[0] - goal[0]) + abs(neighbor_pos[1] - goal[1])  # Manhattan heuristic
                neighbor_node.f = neighbor_node.g + neighbor_node.h  # Total cost

                # Check if a better path exists in the open list
                if any(n for n in open_list if n.position == neighbor_pos and n.g <= neighbor_node.g):
                    continue

                heapq.heappush(open_list, neighbor_node)  # Push neighbor to the open list

    return None  # No path found

# Example grid (0 = walkable, 1 = obstacle)
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 1, 0],
    [0, 0, 0, 0, 0]
]

# Start and goal positions
start = (0, 0)
goal = (4, 4)

# Run A* algorithm
path = astar(grid, start, goal)

# Print the path found
print("Path:", path)
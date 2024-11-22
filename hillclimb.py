import copy
print("Avinash Pandey 21BCT0179")
# Define the goal state for the 8-puzzle
goal_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]  # 0 represents the blank space
]

# Function to calculate the Manhattan distance heuristic
def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:  # Skip the blank space
                goal_x, goal_y = divmod(value - 1, 3)
                distance += abs(i - goal_x) + abs(j - goal_y)
    return distance

# Find the blank space (0) position
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

# Generate all possible moves (neighbors)
def get_neighbors(state):
    neighbors = []
    x, y = find_blank(state)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right
    
    for dx, dy in directions:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:  # Check if within bounds
            new_state = copy.deepcopy(state)
            # Swap the blank with the adjacent tile
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

# Hill Climbing algorithm
def hill_climbing(initial_state):
    current_state = initial_state
    current_cost = manhattan_distance(current_state)
    steps = 0

    while current_cost != 0:  # Continue until the goal is reached
        neighbors = get_neighbors(current_state)
        next_state = None
        next_cost = float('inf')

        # Evaluate all neighbors
        for neighbor in neighbors:
            cost = manhattan_distance(neighbor)
            if cost < next_cost:  # Find the best neighbor
                next_state = neighbor
                next_cost = cost

        # If no improvement, return current state
        if next_cost >= current_cost:
            return current_state, steps, "Reached local maximum or plateau"

        # Move to the better neighbor
        current_state = next_state
        current_cost = next_cost
        steps += 1

    return current_state, steps, "Success"

# Test the algorithm with a sample initial state
initial_state = [
    [2, 8, 3],
    [1, 6, 4],
    [7, 0, 5]
]

solution, steps_taken, status = hill_climbing(initial_state)

print("Initial State:")
for row in initial_state:
    print(row)

print("\nGoal State:")
for row in goal_state:
    print(row)

print(f"\nStatus: {status}")
print(f"Steps Taken: {steps_taken}")

print("\nFinal State:")
for row in solution:
    print(row)

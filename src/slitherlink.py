from pulp import LpProblem, LpVariable, lpSum, LpMinimize, value

# Define the puzzle grid (0 represents empty cells, numbers represent clues)
puzzle = [
    [0, 2, 0, 3],
    [3, 0, 0, 0],
    [0, 0, 0, 0],
    [1, 0, 2, 0],
]

rows = len(puzzle)
cols = len(puzzle[0])

# Create a binary variable for each edge
edges = {(i, j, d): LpVariable(f"edge_{i}_{j}_{d}", cat="Binary") for i in range(rows) for j in range(cols) for d in ["H", "V"]}

# Create the LP problem
prob = LpProblem("Slitherlink", LpMinimize)

# Add the objective function (minimize the total number of edges)
prob += lpSum(edges)

# Add constraints for each clue
for i in range(rows):
    for j in range(cols):
        if puzzle[i][j] > 0:
            prob += lpSum(edges[i, j, d] for d in ["H", "V"]) == puzzle[i][j]

# Add constraints for each cell
for i in range(rows - 1):
    for j in range(cols - 1):
        prob += lpSum(edges[i, j, d] + edges[i + 1, j, d] + edges[i, j + 1, d] + edges[i + 1, j + 1, d] for d in ["H", "V"]) % 2 == 0

# Solve the problem
prob.solve()

# Print the solution
for i in range(rows):
    for j in range(cols):
        if edges[i, j, "H"].value() == 1:
            print("-", end="")
        else:
            print(" ", end="")
        if edges[i, j, "V"].value() == 1:
            print("|", end="")
        else:
            print(" ", end="")
        print(puzzle[i][j] if puzzle[i][j] > 0 else " ", end="")
    print()

# Print the total number of edges used
print("\nTotal number of edges:", int(value(prob.objective)))

import pulp

# Define the matrix A
A = [[4, 3, 1, 4],
    [2, 5, 6, 3],
    [1, 0, 7, 0]]

# Create the LP problem
problem = pulp.LpProblem("Saddle Point LP", pulp.LpMaximize)

# Define the decision variables
x = [pulp.LpVariable(f"x{i}", lowBound=0) for i in range(len(A[0]))]
v1 = pulp.LpVariable("v1")

# Set the objective function
problem += v1

# Add the constraints
for i in range(len(A)):
    problem += v1 <= sum(x[j] * A[i][j] for j in range(len(A[i])))

problem += sum(x) == 1

# Solve the LP problem
problem.solve()

# Get the optimal solution
saddle_point = []
for i in range(len(A)):
    saddle_point.append([x[j].varValue for j in range(len(A[i]))])

# Print the saddle point
print("Saddle Point:")
for row in saddle_point:
    print(row)

# Print the value of the game
print("Value of the game:", pulp.value(problem.objective))

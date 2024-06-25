from pulp import LpMaximize, LpMinimize, LpProblem, LpVariable, value
from fractions import Fraction

model = LpProblem(name="right", sense=LpMaximize)

variables = []
coefficients = [[4, 2, 1], [3, 5, 0], [1, 6, 7], [4, 3, 0]]
for i in range(3):
    variables.append(LpVariable(name=f"x{i+1}", lowBound=0))

v = LpVariable(name="v")

model += v

for i in range(4):
    model += (v <= sum(coefficients[i][j] * variables[j] for j in range(3)), f"constraint{i+1}")

model += sum(variables) == 1

model.solve()

v_value = Fraction(value(v)).limit_denominator()
x_values = [Fraction(value(variables[i])).limit_denominator() for i in range(3)]

print(f"v={v_value}, x={x_values}")

model = LpProblem(name="right", sense=LpMinimize)

variables = []
coefficients = [[4, 3, 1, 4], [2, 5, 6, 3], [1, 0, 7, 0]]
for i in range(4):
    variables.append(LpVariable(name=f"y{i+1}", lowBound=0))

v = LpVariable(name="v")

model += v

for i in range(3):
    model += (v >= sum(coefficients[i][j] * variables[j] for j in range(4)), f"constraint{i+1}")

model += sum(variables) == 1

model.solve()

v_value = Fraction(value(v)).limit_denominator()
y_values = [Fraction(value(variables[i])).limit_denominator() for i in range(4)]

print(f"v={v_value}, y={y_values}")

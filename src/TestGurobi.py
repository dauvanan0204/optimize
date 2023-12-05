# Solve optimize programing by Simplex method
# maximize : 3x + 2y - 4z
# subject to: 
#       x + 4y <= 5
#       2x + 4y -2z <= 6
#       x + y - 2z <= 2

import gurobipy as gp
from gurobipy import GRB

# Create a new model
m = gp.Model()

# Create variable
x = m.addVar(lb = 0, vtype = GRB.CONTINUOUS, name = 'foobar')
y = m.addVar(lb = 0, vtype = GRB.CONTINUOUS)
z = m.addVar(lb = 0, vtype = GRB.CONTINUOUS)

# Set Object funtion
m.setObjective(x + y + z, gp.GRB.MAXIMIZE)

# Add constrains
m.addConstr(0.2*x + 0.4*y+ 0.3*z<= 1160)
m.addConstr(0.3*x + 0.5*y+ 0.4*z<= 1560)
m.addConstr(0.1*x + 0.2*y+ 0.1*z<= 480)

# Solve
m.optimize()
print(f"Optimal objective value: {m.objVal}")
print(f"Solution values: x={x.X}, y={y.X}, z={z.X}")
# Create a new model
# m = gp.Model()

# # Create variable
# x = m.addVar(lb = 0, vtype = GRB.CONTINUOUS, name = 'foobar')
# y = m.addVar(lb = 0, vtype = GRB.CONTINUOUS)
# # z = m.addVar(lb = 0, vtype = GRB.CONTINUOUS)

# # Set Object funtion
# m.setObjective(30*x + 40*y , gp.GRB.MAXIMIZE)

# # Add constrains
# m.addConstr(2*x+y<= 100)
# m.addConstr(x+y<= 70)
# m.addConstr(2*x+2*y<= 120)

# # Solve
# m.optimize()
# print(f"Optimal objective value: {m.objVal}")
# print(f"Solution values: x={x.X}, y={y.X}")

# Solve the following MIP:
#  maximize
#        x +   y + 2 z
#  subject to
#        x + 2 y + 3 z <= 4
#        x +   y       >= 1
#        x, y, z binary


# Create a new model
# m = gp.Model()

# # Create variables
# x = m.addVar(vtype='B', name="x")
# y = m.addVar(vtype='B', name="y")
# z = m.addVar(vtype='B', name="z")

# # Set objective function
# m.setObjective(x + y + 2 * z, gp.GRB.MAXIMIZE)

# # Add constraints
# m.addConstr(x + 2 * y + 3 * z <= 4)
# m.addConstr(x + y >= 1)

# # Solve it!
# m.optimize()

# print(f"Optimal objective value: {m.objVal}")
# print(f"Solution values: x={x.X}, y={y.X}, z={z.X}")


# import gurobipy as gp
# from gurobipy import GRB

# # emptyModel = gp.Model()
# # emptyModel.optimize()
# # vtype:
# # - GRB.CONTINUOUS
# # - GRB.INTEGER
# # - GRB.BINARY
# # lb, ub, vtype, name
# model = gp.Model()
# x = model.addVar(lb = 0, vtype = GRB.CONTINUOUS, name = 'foobar')
# y = model.addVar(lb = 0, vtype = GRB.CONTINUOUS)

# # constrains
# x = model.addConstr(x + y <= 5)
# y = model.addConstr(4*x + y <= 11)

# model.setObjective(2*x + y, sense = GRB.MAXIMIZE)
# model.optimize()


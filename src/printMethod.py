# import gurobipy as gp
# from gurobipy import GRB

# model = gp.Model()
# x = model.addVar(lb = 0, vtype = GRB.CONTINUOUS, name = 'foobar')
# y = model.addVar(lb = 0, vtype = GRB.CONTINUOUS)
# z = model.addVar(lb = 0, vtype = GRB.CONTINUOUS)

# model.addConstr(x + 4*y<= 5)
# model.addConstr(2*x + 4 *y -2*z<= 6)
# model.addConstr(x + y +2*z<= 2)

# model.setObjective(3*x + 2*y -4*z, sense = GRB.MAXIMIZE)
# model.optimize()
# # print(f"Optimal objective value: {model.objVal}")
# # print(model.status)
# print(model.runtime)
# # print(x.X)
# # print(y.X)



import gurobipy as gp
from gurobipy import GRB

# Create a new model
m = gp.Model()

# Create variable
x = m.addVar(lb = 0, vtype = GRB.CONTINUOUS, name = 'foobar')
y = m.addVar(lb = 0, vtype = GRB.CONTINUOUS)
z = m.addVar(lb = 0, vtype = GRB.CONTINUOUS)
t = m.addVar(lb = 0, vtype = GRB.CONTINUOUS)
# z = m.addVar(lb = 0, vtype = GRB.CONTINUOUS)

# Set Object funtion
m.setObjective(x-3*y-3*z+t, gp.GRB.MAXIMIZE)

# Add constrains
m.addConstr(-2*x-y-z-t == -7)
m.addConstr(-3*x+y-z-4*t==-13)
# m.addConstr(z <= 1)
m.addConstr(-x-y-3*z+2*t==-1)
# Solve
m.optimize()
print(f"Optimal objective value: {m.objVal}")
print(f"Solution values: x={x.X}, y={y.X},z={z.X}, t={t.X}")
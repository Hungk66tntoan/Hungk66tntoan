# Github Coplot
# Github Education

import gurobipy as gp
from gurobipy import GRB



model = gp.Model()
#vars = model.addMVar(shape = (10, 10, 10, 10), lb = 0, ub = GRB.INFINITY, vtype = GRB.CONTINUOUS)

x = model.addVar(lb = 0, ub = GRB.INFINITY, vtype = GRB.CONTINUOUS)
y = model.addVar(lb = 0, ub = GRB.INFINITY, vtype = GRB.INTEGER)
z = model.addVar(vtype = GRB.BINARY)

model.addConstr(x+y>=5)
model.addConstr(x+y>=4)

model.setObjective(4*x + 8*y, sense = GRB.MINIMIZE)

model.optimize()
graph = {}
domain = {}

def solve(num_vars, num_constraints, constraints):
    for x_i in range(num_vars):
        domain[x_i] = range(num_vars)
    PQ queue # MRV
    while not queue.isEmpty():
        x_i, x_j = queue.pop():
        if prune(x_i, x_j):
            for


def prune(x_i, x_j):
    removed = False
    for each x in domain[x_i]:
        if
            domain[x].remove()
            removed = True
    return removed


order_slots = []
constraints = {}

# solve: takes in number of variables, constraints, and list of constraints
# returns: approximate ordering
def solve(num_vars, num_constraints, constraints):
    order_slots = range(num_vars)
    # create initial ordering
    wizards = list(constraints.keys())
    for i in range(num_vars):
        order_slots[i] = wizards[i]
    # iteratively remove worst wizard, backtrack at bottom?

# creates constraints - puts constraints into constraints dictionary
# key = wizard out of range, value = wizard ranges
# value: dictionary of each value + range values
def create_constraints(cs):
    for c in cs:
        # if there's something already for the wizard, access it
        if constraints[c[0]]:
            # if there's already something for the 1st wizard constraint, add
            if constraints[c[0]][c[1]]:
                constraints[c[0]][c[1]].append(c[2])
            # create new array of 2nd wizards for 1st wizards
            else:
                constraints[c[0]][c[1]] = [c[2]]
        else:
            constraints[c[0]] = {c[1]:[c[2]]}

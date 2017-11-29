'''
Goal: Solve using some sort of optimization algorithm. Try using simulated
annealing, or something similar such as min-conflicts.

TODO:
Create parser
Create a way to store constraints, names
Create quick way to check constraints
Create heuristic of constraints
Create graph structure?
'''
from scipy import optimize
order_slots = []
curr_errors = []
curr_order = {}
constraints = {}

# solve: takes in number of variables, constraints, and list of constraints
# returns: approximate ordering
def solve(num_vars, cs):
    global order_slots
    order_slots = [0] * num_vars
    global curr_errors
    curr_errors = [0] * num_vars
    print(len(curr_errors))
    # create initial ordering
    create_constraints(cs)
    wizards = list(constraints.keys())
    for i in range(num_vars):
        order_slots[i] = wizards[i]
        curr_order[wizards[i]] = i

    # check for errors, put num of errors in list in order
    check_constraints(order_slots)
    # exchange worst + random amount based on heat coefficient
    ret = optimize.anneal(check_constraints, curr_order, schedule='boltzmann', full_output=True, maxiter=500, lower=-10, upper=10, dwell=250, disp=True)
    return ret


# creates constraints - puts constraints into constraints dictionary
# key = wizard out of range, value = wizard ranges
# value: dictionary of each value + range values
def create_constraints(cs):
    for c in cs:
        # if there's something already for the wizard, access it
        if c[0] in constraints:
            # if there's already something for the 1st wizard constraint, add
            if c[1] in constraints[c[0]]:
                constraints[c[0]][c[1]].append(c[2])
            # create new array of 2nd wizards for 1st wizards
            else:
                constraints[c[0]][c[1]] = [c[2]]
        else:
            constraints[c[0]] = {c[1]:[c[2]]}

def check_constraints(order):
    # check iteratively if wizard satisfies constraints
    print(len(curr_errors))
    for i in list(range(len(order))):
        wizard = order[i]
        errors = 0
        for c in list(constraints[wizard].keys()):
            for other_wiz in constraints[wizard][c]:
                # check to see if wizard fails constraints starting w each key
                if (i < curr_order[c] and i > curr_order[other_wiz]) or (i > curr_order[c] and i < curr_order[other_wiz]):
                    errors += 1
        curr_errors[i] = errors
    return sum(curr_errors)

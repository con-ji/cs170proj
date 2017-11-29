'''
Goal: Solve using some sort of optimization algorithm. Try using simulated
annealing, or something similar such as min-conflicts.

'''
from scipy import optimize
from random import shuffle
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
    # create initial ordering
    get_wizards(num_vars, cs)
    create_constraints(cs)
    shuffle(order_slots)

    # check for errors, put num of errors in list in order
    # exchange worst + random amount based on heat coefficient
    ret = optimize.basinhopping(check_constraints, order_slots)
    return ret

def get_wizards(num_vars, cs):
    wizards = 0
    global order_slots
    while wizards < num_vars:
        for c in cs:
            if c[0] not in curr_order:
                curr_order[c[0]] = wizards
                order_slots[wizards] = c[0]
                wizards += 1
            if c[1] not in curr_order:
                curr_order[c[1]] = wizards
                order_slots[wizards] = c[1]
                wizards += 1
            if c[2] not in curr_order:
                curr_order[c[2]] = wizards
                order_slots[wizards] = c[2]
                wizards += 1

# creates constraints - puts constraints into constraints dictionary
# key = wizard out of range, value = wizard ranges
# value: dictionary of each value + range values
def create_constraints(cs):
    for c in cs:
        # if there's something already for the wizard, access it
        if c[2] in constraints:
            # if there's already something for the 1st wizard constraint, add
            if c[0] not in constraints[c[2]]:
                constraints[c[2]][c[0]] = [c[1]]
            # create new array of 2nd wizards for 1st wizards
            else:
                constraints[c[2]][c[0]].append(c[1])
        else:
            constraints[c[2]] = {c[0]:[c[1]]}

def check_constraints(order):
    # check iteratively if wizard satisfies constraints
    global curr_order
    for i in range(len(order)):
        curr_order[order[i]] = i
    for i in range(len(order)):
        wizard = order[i]
        errors = 0
        if wizard in constraints:
            for c in list(constraints[wizard].keys()):
                for other_wiz in constraints[wizard][c]:
                    # check to see if wizard fails constraints starting w each key
                    if (i < curr_order[c] and i > curr_order[other_wiz]) or (i > curr_order[c] and i < curr_order[other_wiz]):
                        errors += 1
        curr_errors[i] = errors
    return sum(curr_errors)

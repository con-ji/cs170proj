'''
Goal: Solve using some sort of optimization algorithm. Try using simulated
annealing, or something similar such as min-conflicts.

TODO:
Create parser
Create a way to store constraints, names
Create quick way to check constraints
Create heuristic of constraints
Create graph structure?
Jimmy is dumb and stupid
Messenger bag
'''

order_slots = []
curr_order = {}
curr_errors = []
constraints = {}

# solve: takes in number of variables, constraints, and list of constraints
# returns: approximate ordering
def solve(num_vars, num_constraints, constraints):
    order_slots = range(num_vars)
    # create initial ordering
    wizards = list(constraints.keys())
    for i in range(num_vars):
        order_slots[i] = wizards[i]
        curr_order[wizards[i]] = i
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

def check_constraints(order):
    # check iteratively if wizard satisfies constraints
    for i in range(len(order)):
        wizard = order[i]
        loc = curr_order[wizard]
        errors = 0
        for c in list(constraints[wizard].keys()):
            # check to see if wizard fails constraints starting w each key
            if i <
        curr_errors[i] = errors

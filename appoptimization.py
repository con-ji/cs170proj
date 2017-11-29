'''
Goal: Solve using some sort of optimization algorithm. Try using simulated
annealing, or something similar such as min-conflicts.

Will be replaced by simannealsolve.py
'''
import numpy as np
from scipy import optimize
from random import shuffle

order_slots = []
curr_errors = []
# number:wizard
wizard_dict = {}
# wizard:number
dict_wizard = {}
constraints = {}
# wizard number:location
curr_loc = {}

# solve: takes in number of variables, constraints, and list of constraints
# returns: approximate ordering
def solve(num_vars, cs):
    global order_slots
    order_slots = list(range(num_vars))
    global curr_errors
    curr_errors = np.zeros(num_vars)
    global wizard_dict
    global dict_wizard
    # create initial ordering
    get_wizards(num_vars, cs)
    create_constraints(cs)
    wizard_dict = {value: key for key, value in dict_wizard.items()}
    shuffle(order_slots)
    # check for errors, put num of errors in list in order
    ret = optimize.basinhopping(check_constraints, order_slots, T=3, stepsize=1, interval = 1)
    return np.array_str(ret.x)

def get_wizards(num_vars, cs):
    wizards = 0
    for c in cs:
        if c[0] not in dict_wizard:
            dict_wizard[c[0]] = wizards
            wizards += 1
            if wizards >= num_vars:
                break
        if c[1] not in dict_wizard:
            dict_wizard[c[1]] = wizards
            wizards += 1
            if wizards >= num_vars:
                break
        if c[2] not in dict_wizard:
            dict_wizard[c[2]] = wizards
            wizards += 1
            if wizards >= num_vars:
                break

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
    global curr_loc
    for i in range(len(order)):
        curr_loc[i] = i
    for i in range(len(order)):
        wizard = order[i]
        errors = 0.0
        if wizard_dict[int(wizard)] in constraints:
            for c in list(constraints[wizard_dict[int(wizard)]].keys()):
                for other_wiz in constraints[wizard_dict[int(wizard)]][c]:
                    # check to see if wizard fails constraints
                    if (i < curr_loc[dict_wizard[c]]
                     and i > curr_loc[dict_wizard[other_wiz]]) or (i > curr_loc[dict_wizard[c]]
                     and i < curr_loc[dict_wizard[other_wiz]]):
                        errors += 1
        curr_errors[i] = errors
    return sum(curr_errors)

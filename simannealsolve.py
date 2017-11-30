'''
Uses simulated annealing to solve this. For realsies this time.

Credit to: https://github.com/perrygeo/simanneal

TODO:
Bring over constraint generation from appoptimization
Call from parsing
Anneal parameters
Create a move function - in this case, some sort of swap/permute
Create an objective function/energy - number of incorrect constraints
Create a more efficient way to check constraints - remove duplicates
'''

from simanneal import Annealer
import math
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

class WizardConstraints(Annealer):
    # Test annealer with CS170 WizardConstraints project

    # creates a new random permutation of the list
    # exchange pairwise randomly, or by worst + random?
    # currently: worst + random
    def move(self):


    # objective function - minimize total sum of errors
    def energy(self):
        global curr_loc
        for i in range(len(order)):
            curr_loc[i] = i
        for i in range(len(order)):
            wizard = order[i]
            errors = 0
            if wizard_dict[wizard] in constraints:
                for c in list(constraints[wizard_dict[wizard]].keys()):
                    for other_wiz in constraints[wizard_dict[wizard]][c]:
                        # check to see if wizard fails constraints
                        if (i < curr_loc[dict_wizard[c]]
                         and i > curr_loc[dict_wizard[other_wiz]]) or (i > curr_loc[dict_wizard[c]]
                         and i < curr_loc[dict_wizard[other_wiz]]):
                            errors += 1
            curr_errors[i] = errors
        return sum(curr_errors)

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

def solve(num_vars, constraints):
    create_constraints(constraints)
    initial_state = get_wizards(num_vars, constraints)
    wizard_solver = WizardConstraints(initial_state)
    auto_schedule = wizard_solver.auto(minutes=1,steps=1000000)
    wizard_solver.set_schedule(auto_schedule)
    wizard_solver.copy_strategy = "slice"
    state, x = wizard_solver.anneal()
    print(wizard_solver.energy())
    return state

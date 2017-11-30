'''
Uses simulated annealing to solve this. For realsies this time.
Simulated Annealing Python Library: https://github.com/perrygeo/simanneal

TODO:
input20_3.in
input35_4.in
'''
import simannealsolve
import sys
from simanneal import Annealer
import math
import random

class WizardConstraints(Annealer):
    def __init__(self, state, num_vars, constraints):
        self.num_vars = num_vars
        self.curr_errors = [0] * num_vars
        self.constraints = constraints
        super(WizardConstraints, self).__init__(state)

    def move(self):
        # random swaps now xd
        swaps = random.sample(range(self.num_vars), 2)
        self.state[swaps[0]], self.state[swaps[1]] = self.state[swaps[1]], self.state[swaps[0]]

    # objective function - minimize total sum of errors
    def energy(self):
        # current location of each wizard
        curr_loc = {}
        for i in range(len(self.state)):
            curr_loc[self.state[i]] = i
        # iterate through constraints, checking each
        errors = 0
        for c in self.constraints:
            w1, w2, w3 = c[0], c[1], c[2]
            # check if w3 out of w1, w2 range
            if (curr_loc[w3] > curr_loc[w1] and \
                curr_loc[w3] < curr_loc[w2]):
                errors += 1
            elif (curr_loc[w3] < curr_loc[w1] and \
                curr_loc[w3] > curr_loc[w2]):
                errors += 1
        return errors

def get_wizards(num_vars, cs):
    wizards = set()
    for c in cs:
        wizards.add(c[0])
        wizards.add(c[1])
        wizards.add(c[2])
    return list(wizards)

def solve(num_vars, constraints):
    init_state = get_wizards(num_vars, constraints)
    wizard_solver = WizardConstraints(init_state, num_vars, constraints)
    auto_schedule = wizard_solver.auto(minutes=15,steps=150000)
    wizard_solver.set_schedule(auto_schedule)
    wizard_solver.copy_strategy = "slice"
    state, x = wizard_solver.anneal()
    print(wizard_solver.energy())
    return state

'''
Parse the input file, call the methods and return the result.
'''

def parse(input_file):
    inputs = open(input_file, "r")
    result = open("output" + str(input_file[-7:-3]) + ".in", "w")

    input_list = inputs.readlines()
    inputs.close()
    num_vars = int(input_list[0])
    num_constraints = int(input_list[1])
    input_list = [line.split() for line in input_list[2:]]

    for s in simannealsolve.solve(num_vars, input_list):
        result.write(s + " ")
    result.close()

if __name__ == '__main__':
    parse(sys.argv[1])

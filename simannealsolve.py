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

class WizardConstraints(Annealer):
    # Test annealer with CS170 WizardConstraints project
    def move(self):

    def energy(self):

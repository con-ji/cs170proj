from Numberjack import *

wizard_dict = {}

def model_wizards(wizards, constraints):
    # each item is mapped to a domain of possible values: each wizard -> slot
    # one variable for each wizard, domain of possible values for each
    # order = VarArray(len(wizards), range(len(wizards)), 'w')
    # must compare current location of each wizard and compare against the other
    # each item in order: w_ and its locations
    global wizard_dict
    order = VarArray(0)
    for w in wizards:
        # make new variable for each wizard
        v = Variable(range(len(wizards)), w)
        wizard_dict[w] = v
        order.append(v)
    model = Model(
            AllDiff(order),
            [(wizard_dict[c[2]].get_value() > wizard_dict[c[0]].get_value() and \
            wizard_dict[c[2]].get_value() > wizard_dict[c[1]].get_value()) or \
            (wizard_dict[c[2]].get_value() < wizard_dict[c[0]].get_value() and \
            wizard_dict[c[2]].get_value() < wizard_dict[c[1]].get_value()) \
            for c in constraints]
    )
    return (order, model)

def solve_wizards(param):
    (order, model) = model_wizards(param['wizards'], param['constraints'])
    solver = model.load(param['solver'])
    solver.solve()
    return [str(Expression.get_value(i)) for i in order]

def get_wizards(cs):
    wizards = set()
    for c in cs:
        wizards.add(c[0])
        wizards.add(c[1])
        wizards.add(c[2])
    wizards = list(wizards)
    return wizards

'''
Parse the input file, call the methods and return the result.
'''
def parse(input_file):
    inputs = open(input_file, "r")
    result = open("output" + str(input_file[-7:-3]) + ".out", "w")

    input_list = inputs.readlines()
    inputs.close()
    num_vars = int(input_list[0])
    num_constraints = int(input_list[1])
    input_list = [line.split() for line in input_list[2:]]
    wizards = get_wizards(input_list)

    for s in solve_wizards(input({'solver':'Mistral', 'wizards':wizards, \
                                  'constraints':input_list})):
        result.write(s + " ")
    result.close()

if __name__ == '__main__':
    parse(sys.argv[1])

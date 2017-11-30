from Numberjack import *

def model_wizards(wizards, constraints):
    order = VarArray(wizards)
    indices = {wizards[i]:i for i in range(len(wizards))}
    model = Model(
            AllDiff(order),
            [(order[indices[c[2]]] > order[indices[c[0]]] and \
            order[indices[c[2]]] > order[indices[c[1]]]) or \
            (order[indices[c[2]]] < order[indices[c[0]]] and \
            order[indices[c[2]]] < order[indices[c[1]]]) \
            for c in constraints]
    )
    return (order, model)

def solve_wizards(param):
    (order, model) = model_wizards(param['wizards'], param['constraints'])
    solver = model.load(param['solver'])
    solver.solve()
    return solver.get_solution()

def get_wizards(cs):
    wizards = set()
    for c in cs:
        wizards.add(c[0])
        wizards.add(c[1])
        wizards.add(c[2])
    return list(wizards)

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

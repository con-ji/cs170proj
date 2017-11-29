'''
Parse the input file, call the methods and return the result.
'''
import appoptimization

def parse():
    inputs = open("input.in", "r")
    result = open("output.in", "w")

    input_list = inputs.readlines()
    num_vars = int(input_list[0])
    num_constraints = int(input_list[1])
    input_list = [line.split() for line in input_list[2:]]

    inputs.close()
    result.write(appoptimization.solve(num_vars, num_constraints, input_list))
    result.close()

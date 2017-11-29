'''
Parse the input file, call the methods and return the result.
'''
import appoptimization
import sys

def parse(input_file):
    inputs = open(input_file, "r")
    result = open("output.in", "w")

    input_list = inputs.readlines()
    num_vars = int(input_list[0])
    num_constraints = int(input_list[1])
    input_list = [line.split() for line in input_list[2:]]

    inputs.close()
    result.write(appoptimization.solve(num_vars, input_list))
    result.close()

if __name__ == '__main__':
    parse(sys.argv[1])

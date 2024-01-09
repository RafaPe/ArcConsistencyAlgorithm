from ArcConsistency import Variable, Constraint, AC3
from itertools import product

def variables_definition(values):
    variables = {}

    for item in values:
        variables[item[0]] = Variable(*item)

    return variables

def constraints_definition(values):
    constraints = {}

    for item in values:
        constraints[item[0]] = Constraint(*item)

    return constraints

def c1(x1, x2, x3, x4, x5, x6, x7, x8):
    sums = [
        x1 + x2 + x3 + x4,
        x5 + x6 + x7 + x8,
        x2 + x3 + x6 + x7,
        x3 + x4 + x7 + x8,
        x1 + x4 + x5 + x8,
        x4 + x3 + x7 + x8
    ]
    return len(set(sums)) == 1
    
def c2(x1, x2, x3, x4, x5, x6, x7, x8):
    return len(set([x1, x2, x3, x4, x5, x6, x7, x8])) == 8

def solution_search(variables):
    solutions = []
    for combination in product(*[variables[v].domain for v in variables]):
        dict_values = dict(zip(variables.keys(), combination))

        if all([
            c1(dict_values['X1'], dict_values['X2'], dict_values['X3'], dict_values['X4'], dict_values['X5'], dict_values['X6'], dict_values['X7'], dict_values['X8']),
            c2(dict_values['X1'], dict_values['X2'], dict_values['X3'], dict_values['X4'], dict_values['X5'], dict_values['X6'], dict_values['X7'], dict_values['X8'])
        ]):
            solutions.append(dict_values)
    return solutions


def main():
    variable_values = [
        ['X1', [1,2,3,4,5,6,7,8]],
        ['X2', [1,2,3,4,5,6,7,8]],
        ['X3', [4]],
        ['X4', [1]],
        ['X5', [1,2,3,4,5,6,7,8]],
        ['X6', [1,2,3,4,5,6,7,8]],
        ['X7', [1,2,3,4,5,6,7,8]],
        ['X8', [6]]
    ]

    constraint_values = [ 
        ['C1', ['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8'], c1],
        ['C2', ['X1', 'X2', 'X3', 'X4', 'X5', 'X6', 'X7', 'X8'], c2]
    ]

    
    variables = variables_definition(variable_values)
    constraints = constraints_definition(constraint_values)

    variables = AC3(variables, constraints)

    solutions = solution_search(variables)

    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()
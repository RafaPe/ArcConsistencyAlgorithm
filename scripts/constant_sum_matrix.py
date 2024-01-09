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

def c1(A, B, C):
    return B+1 == A+2 and B+1 == C+4 and A+2 == C+4
    
def c2(A, B, C):
    return A + 5 == B + C + 2

def solution_search(variables):
    solutions = []
    for combination in product(*[variables[v].domain for v in variables]):
        dict_values = dict(zip(variables.keys(), combination))

        if all([
            c1(dict_values['A'], dict_values['B'], dict_values['C']),
            c2(dict_values['A'], dict_values['B'], dict_values['C']),
        ]):
            solutions.append(dict_values)
    return solutions


def main():
    variable_values = [
        ['A', [1,2,3,4,5]],
        ['B', [1,2,3,4,5]],
        ['C', [1,2,3,4,5]]
    ]

    constraint_values = [ 
        ['C1', ['A','B','C' ], c1],
        ['C2', ['A','B','C' ], c2]
    ]

    
    variables = variables_definition(variable_values)
    constraints = constraints_definition(constraint_values)

    variables = AC3(variables, constraints)

    solutions = solution_search(variables)

    for solution in solutions:
        print(solution)

if __name__ == "__main__":
    main()
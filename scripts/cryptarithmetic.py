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

def c1(O, X, R):
    return O * 2 == (10 * X) + R

def c2(X, W, Y, U):
    return X + (W * 2) == (10 * Y) + U

def c3(Y, T, Z, O):
    return Y + (T * 2) == (10 * Z) + O

def c4(Z, F):
    return Z == F

def c5(T, W, O, F, U, R):
    return len(set([T, W, O, F, U, R])) == 6

def solution_search(variables):
    solutions = []
    for combination in product(*[variables[v].domain for v in variables]):
        dict_values = dict(zip(variables.keys(), combination))

        if all([
            c1(dict_values['O'], dict_values['X'], dict_values['R']),
            c2(dict_values['X'], dict_values['W'], dict_values['Y'], dict_values['U']),
            c3(dict_values['Y'], dict_values['T'], dict_values['Z'], dict_values['O']),
            c4(dict_values['Z'], dict_values['F']),
            c5(dict_values['T'], dict_values['W'], dict_values['O'], dict_values['F'], dict_values['U'], dict_values['R'])
        ]):
            solutions.append(dict_values)
    return solutions

def answer_print_format(selected_values):
    two  = 100*selected_values['T'] + 10*selected_values['W'] + selected_values['O']
    four = 1000*selected_values['F'] + 100*selected_values['O'] + 10*selected_values['U'] + selected_values['R']
    print( "TWO = {} \t FOUR = {}".format(two,four) )

def main():
    variable_values = [
        ['T', [1,2,3,4,5,6,7,8,9]],
        ['W', [0,1,2,3,4,5,6,7,8,9]],
        ['O', [0,1,2,3,4,5,6,7,8,9]],
        ['F', [1,2,3,4,5,6,7,8,9]],
        ['U', [0,1,2,3,4,5,6,7,8,9]],
        ['R', [0,1,2,3,4,5,6,7,8,9]],
        ['X', [0,1]],
        ['Y', [0,1]],
        ['Z', [0,1]],
    ]

    constraint_values = [ 
        ['C1', ['O','X','R' ], c1],
        ['C2', ['X', 'W', 'Y', 'U' ], c2],
        ['C3', ['Y', 'T', 'Z', 'O' ], c3],
        ['C4', ['Z', 'F' ], c4],
        ['C5', ['T','W','O','F','U','R'], c5],
    ]
    
    variables = variables_definition(variable_values)
    constraints = constraints_definition(constraint_values)

    variables = AC3(variables, constraints)

    solutions = solution_search(variables)

    for solution in solutions:
        answer_print_format(solution)

if __name__ == "__main__":
    main()
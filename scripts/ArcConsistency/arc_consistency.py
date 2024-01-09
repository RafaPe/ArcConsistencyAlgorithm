from itertools import product
from collections import deque
from typing import List, Callable, Dict

class Variable:
    def __init__(self, id_: str, domain: List[int]):
        self.id = id_
        self.domain = domain
    def __str__(self):
        return f'{self.id} -> {self.domain}'


class Constraint:
    def __init__(self, id_: str, rel_variables: List[Variable], func: Callable):
        self.id = id_
        self.related_variables = rel_variables
        self.function = func

def AC3(variables: Dict[str,Variable], constraints: Dict[str,Constraint]):
    edges = []
    for key in constraints:
        for var in constraints[key].related_variables:
            if (var, key) not in edges:
                edges.append((var, key))
        
    edges_deque = deque(edges)
    while(edges_deque):
        variable_name, constraint_name = edges_deque.popleft()
        
        for value in list(variables[variable_name].domain):
            valid = False
            for combination in product(*[variables[v].domain if v != variable_name else [value] for v in constraints[constraint_name].related_variables]):
                if constraints[constraint_name].function(*combination):
                    valid = True
                    break

            if not valid:            
                variables[variable_name].domain.remove(value)
                related_cons = [constrain for variable, constrain in edges if variable == variable_name]
                affected_edges = [(v, c) for v, c in edges if c in related_cons and v != variable_name]
                edges_deque += deque(affected_edges)

    return variables

if __name__ == "__main__":
    pass
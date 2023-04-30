import numpy as np
from platypus import NSGAII, Problem, Real
from cec2017 import functions


def fun(x):
    x = np.array(x).reshape(2, 10)
    f = np.empty(len(x))
    i = 2
    # refatorar esse for, essa variavel 'a', acho q era pra ser um vetor
    for xi in enumerate(x):
        a = functions.all_functions[i](x)
    return a


problem = Problem(20, 2)
problem.types[:] = Real(-100, 100)
problem.function = fun
problem.directions[:] = Problem.MINIMIZE

algorithm = NSGAII(problem)
algorithm.run(10000)

print("Solução:", algorithm.result[0].variables, "Valor da função objetivo:", algorithm.result[0].objectives[0])
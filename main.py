import numpy as np
from platypus import NSGAII, Problem, Real, Hypervolume, calculate, display, experiment
from cec2017 import functions

num_runs = 1
budget_multiplier = 10000

def fun(x):
    x = np.array(x).reshape(2, 10)
    f = np.empty(len(x))
    i = 2
    for xi in enumerate(x):
        a = functions.all_functions[i](x)
    return a

problem = Problem(20, 2)
problem.types[:] = Real(-100, 100)
problem.function = fun
#problem.function = functions.all_functions[2]
problem.directions[:] = Problem.MINIMIZE
algorithm = NSGAII

# problem = [DTLZ2(3)]
# algorithm = [NSGAII, (NSGAIII, {"divisions_outer":12})]

results = experiment(algorithm, problem, nfe=(1 * budget_multiplier))
#print(results)

# Análise dos resultados para essa dimensão
hyp = Hypervolume(minimum=[0, 0], maximum=[1, 1])
hyp_result = calculate(results, hyp)
display(hyp_result, ndigits=3)



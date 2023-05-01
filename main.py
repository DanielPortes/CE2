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


# import numpy as np
# from platypus import NSGAII, Problem, Real, Hypervolume, calculate,display
# from cec2017 import functions

# num_runs = 1
# budget_multiplier = 10000

# def fun(x):
#     x = np.array(x).reshape(2, 10)
#     f = np.empty(len(x))
#     i = 2
#     for xi in enumerate(x):
#         a = functions.all_functions[i](x)
#     return a

# for dimension in range(1, 2):
#     problem = Problem(20, 2)
#     problem.types[:] = Real(-100, 100)
#     problem.function = fun
#     problem.directions[:] = Problem.MINIMIZE

#     results = []
#     for i in range(num_runs):
#         budget = dimension * budget_multiplier
#         algorithm = NSGAII(problem, budget=budget)
#         algorithm.run(budget)
#         results.append(algorithm.result)

#     # Análise dos resultados para essa dimensão
#     hyp = Hypervolume(minimum=[0, 0], maximum=[1, 1])
#     hyp_result = calculate(results, hyp)
#     display(hyp_result, ndigits=2)



# import numpy as np
# from platypus import NSGAII, Problem, Real
# from cec2017 import functions

# num_runs = 51
# budget_multiplier = 10000

# def fun(x):
#     x = np.array(x).reshape(2, 10)
#     f = np.empty(len(x))
#     i = 2
#     for xi in enumerate(x):
#         a = functions.all_functions[i](x)
#     return a

# for dimension in range(1, 2):
#     problem = Problem(dimension * 20, 2)
#     problem.types[:] = Real(-100, 100)
#     problem.function = fun
#     problem.directions[:] = Problem.MINIMIZE

#     results = []
#     for i in range(num_runs):
#         budget = dimension * budget_multiplier
#         algorithm = NSGAII(problem, budget=budget)
#         algorithm.run(budget)
#         results.append(algorithm.result)

#     # Análise dos resultados para essa dimensão
#     # ...

#     print("Dimensão:", dimension)



# import numpy as np
# from platypus import NSGAII, Problem, Real
# from cec2017 import functions


# def fun(x):
#     x = np.array(x).reshape(2, 10)
#     f = np.empty(len(x))
#     i = 2
#     # refatorar esse for, essa variavel 'a', acho q era pra ser um vetor
#     for xi in enumerate(x):
#         a = functions.all_functions[i](x)
#     return a


# problem = Problem(20, 2)
# problem.types[:] = Real(-100, 100)
# problem.function = fun
# problem.directions[:] = Problem.MINIMIZE

# algorithm = NSGAII(problem)
# algorithm.run(10000)

# print("Solução:", algorithm.result[0].variables, "Valor da função objetivo:", algorithm.result[0].objectives[0])
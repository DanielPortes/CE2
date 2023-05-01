import numpy as np
from platypus import *
from cec2017 import functions



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
problem.directions[:] = Problem.MINIMIZE
algorithm = NSGAII

num_runs = 1
budget_multiplier = 10
n_runs = 1
results = []
# solutions = []
solutions_list = []

for i in range(n_runs):
    algorithm = NSGAII
    value = experiment(algorithm, problem, nfe=(1 * budget_multiplier), seeds=1)
    # print(value.get("NSGAII").get("Problem")[0][0])
    solutions_list.append(value.get("NSGAII").get("Problem")[0][0].variables)

lista = []
for i in range(len(solutions_list)):
    lista = solutions_list[i]
print(lista)

# mean and std from lista
mean = np.mean(lista, axis=0)
std = np.std(lista, axis=0)
print(mean)
print(std)







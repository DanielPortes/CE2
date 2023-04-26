from platypus import NSGAII, Problem, Real
import cec2017.functions as functions

problem = Problem(1, 1)
problem.types[:] = Real(-10, 10)
problem.function = functions.f3
problem.directions = -1

algorithm = NSGAII(problem)
algorithm.run(10000)

print(algorithm.result[0].objectives[0])




import numpy as np
from platypus import *
from cec2017 import functions
import matplotlib.pyplot as plt

vetorY = []

def fun(x):
    x = np.array(x).reshape(2, 10)
    f = np.empty(len(x))
    i = 3
    for xi in enumerate(x):
        a = functions.all_functions[i](x)
    return a

def fun2(x):
    x = np.array(x).reshape(2, 2)
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

budget_multiplier = 10
n_runs = 1
results = []
solutions_list = []
dim = 10
maior = 0
menor = 100 


for i in range(n_runs):
    algorithm = NSGAII
    value = experiment(algorithm, problem, nfe=(dim * budget_multiplier), seeds=1)
    solutions_list.append(value.get("NSGAII").get("Problem")[0][i].variables)
    valor = fun(value.get("NSGAII").get("Problem")[0][i].variables)
    for j in range(len(valor)):
        vetorY.append(valor[j])
        
lista = []
for i in range(len(solutions_list)):
    lista = solutions_list[i]

for i in range(len(lista)):
    if(maior < lista[i]):
        maior = lista[i]

    if(menor > lista[i]):
         menor = lista[i]


# mean and std from lista
mean = np.mean(lista, axis=0)
median = np.median(lista, axis=0)
std = np.std(lista, axis=0)
print("media: ",mean)
print("mediana: ",median)
print("desvio padrao: ",std)
print("maior: ", maior)
print("menor: ",menor)

print("------------------------------------")

problem = Problem(4, 2)
problem.types[:] = Real(-100, 100)
problem.function = fun2
problem.directions[:] = Problem.MINIMIZE
algorithm = NSGAII

budget_multiplier = 10
n_runs = 1
results = []
solutions_list = []
dim = 2
maior = 0
menor = 100


for i in range(n_runs):
    algorithm = NSGAII
    value = experiment(algorithm, problem, nfe=(dim * budget_multiplier), seeds=1)
    solutions_list.append(value.get("NSGAII").get("Problem")[0][i].variables)
    valor = fun2(value.get("NSGAII").get("Problem")[0][i].variables)
    for j in range(len(valor)):
        vetorY.append(valor[j])

lista = []
for i in range(len(solutions_list)):
    lista = solutions_list[i]

for i in range(len(lista)):
    if(maior < lista[i]):
        maior = lista[i]

    if(menor > lista[i]):
         menor = lista[i]

# mean and std from lista
mean2 = np.mean(lista, axis=0)
median2 = np.median(lista, axis=0)
std2 = np.std(lista, axis=0)
print("media: ",mean2)
print("mediana: ",median2)
print("desvio padrao: ",std2)
print("maior: ", maior)
print("menor: ",menor)


# Plotando o gráfico
plt.plot(vetorY)

# Personalizando o gráfico
plt.title("Gráfico de y")
plt.xlabel("Índice")
plt.ylabel("Valor de y")

# Mostrando o gráfico
plt.show()







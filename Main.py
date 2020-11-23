from DAG_Generator import*
from Greedy_Algorithm import*

time = 0
k = 8 #number of processors
n = 100 #number of tasks
lim = 5 #limit
nullChance = 5 #Percent Chance for any given node to be null/root
units, preds, comps = generate(n, lim, nullChance)

print("Units: " + str(units))
print("Predecessors: " + str(preds))
print("Completed[s]: " + str(comps))
print("Processor[s]: " + str(k))

print()
print("Base Greedy Approach:")
greedySolve(units, preds, comps, time, k)


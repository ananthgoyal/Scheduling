from DAG_Generator import*
from Greedy_Algorithm import*
from Brute_Force import*
time = 0
k = 4

units, preds, comps = generate(20, 4)
print("Units: " + str(units))
print("Predecessors: " + str(preds))
print("Completed[s]: " + str(comps))
print("Processor[s]: " + str(k))

print()
print("Base Greedy Approach:")
greedySolve(units, preds, comps, time, k)

print()
print("Greedy Step(s) Approach:")

print()
print("Brute Force Approach:")


units = [0, 1, 2, 3, 4, 5, 6, 7, 8]
preds = [[], [0], [0], [0, 1, 2], [1, 5], [], [], [3, 4, 6], [2, 3, 7]]
comps = [0, 0, 0, 0, 0, 0, 0, 0, 0]
time = 0
k = 3

def solve(units, preds, comps, time, k):
    start = 0
    cache = []
    time = rootSolve(units, preds, comps, time, k)
    while solveCheck(comps) == 0:
        for j in range(0, k):
            for i in range(start, len(units)):
                if i+1 == len(units):
                    break
                if len(preds[i+1]) == 0:
                    pass
                elif check(comps, preds, i+1) == 1:
                    if commonVal(cache, preds[i+1]):
                        break
                    comps[units[i+1]] = 1
                    cache.append(units[i+1])
                    start = units[i+1]
                    break
        cache.clear()
        time += 1
    print("Moves/Time:" + str(time))

#solve time for all root nodes
def rootSolve(units, preds, comps, time, k):
    start = 0
    while rootCheck(units, preds, comps) == 0:
        for j in range(0, k):
            for i in range(start, len(preds)):
                if len(preds[units[i]]) == 0:
                    comps[units[i]] = 1
                    if i+1 == len(units):
                        break
                    start = units[i+1]
                    break
        time += 1
    return time

#check if all predecessors are scheduled
def check(comps, preds, n):
    val = 1
    for i in range(0, len(preds[n])):
        val *= comps[preds[n][i]]
    return val

#check if solved globally
def solveCheck(comps):
    val = 1
    for i in range(0, len(comps)):
        val *= comps[i]
    return val

#check if roots are solved
def rootCheck(units, preds, comps):
    val = 1
    for i in range(0, len(preds)):
        if len(preds[units[i]]) == 0:
            if comps[units[i]] == 1:
                val *= 1
            else:
                val *= 0
    return val

#find common val in two lists
def commonVal(list1, list2):
    for x in list1:
        for y in list2:
            if x == y:
                return True
    return False

solve(units, preds, comps, time, k)

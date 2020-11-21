import random

def generate(n, lim, nullChance):
    units, preds, comps, cache = [], [], [], []
    for i in range (0, n):
        units.append(i)
        comps.append(0)
    preds.append([])
    for i in range(1, n):
        for x in range(0, lim):
            val = random.randrange(0, i)
            if val not in cache:
                cache.append(val)
        if random.randrange(0, 100) < nullChance:
           preds.append([])
        else:
            preds.append(cache)
        cache = []
    return units, preds, comps



import random
def generate(n, lim):
    units = []
    preds = []
    comps = []
    val = 0
    cache = []
    for i in range (0, n):
        units.append(i)
        comps.append(0)
    preds.append([])
    for i in range(1, n):
        for x in range(0, lim):
            val = random.randrange(0, i)
            if val not in cache:
                cache.append(val)
        preds.append(cache)
        cache = []
    return units, preds, comps




generate(10, 4)
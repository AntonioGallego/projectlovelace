def logistic_map(r):
    L = []
    x = 0.5
    for i in range(51):
        L.append(x)
        x = r * x * (1 - x)
    return L
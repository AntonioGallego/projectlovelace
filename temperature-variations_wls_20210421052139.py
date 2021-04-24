from math import sqrt

def temperature_statistics(T):
    mean = sum(T) / len(T)
    std  = 0
    for t in T:
        std+=(t-mean)**2
    std=sqrt(std/len(T))
    return mean, std
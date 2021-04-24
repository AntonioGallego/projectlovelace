from math import sqrt

def habitable_exoplanet(L, r):
    rI=sqrt(L/1.1)
    rO=sqrt(L/0.54)
    if r>rO:
        habitability = 'too cold'
    elif r<rI:
        habitability = 'too hot'
    else:
        habitability = 'just right'
    return habitability
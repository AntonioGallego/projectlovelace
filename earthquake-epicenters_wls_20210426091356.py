# Formulae http://www.ambrsoft.com/TrigoCalc/Circles2/circle2intersection/CircleCircleIntersection.htm

from math import sqrt

pWaveSpeed = 6

def whichEquals(a,b,c,d):
    a,b,c,d=round(a,7),round(b,7),round(c,7),round(d,7)
    if a==b or a==c or a==d:
        return a
    elif b==c or b==d:
        return b
    else:
        return c

def center(x1,y1,r1,x2,y2,r2):
    d = sqrt( (x2-x1)**2 + (y2-y1)**2 )
    area = .25 * sqrt((d+r1+r2) * (d+r1-r2) * (d-r1+r2) * (-d+r1+r2))
    x0p = ((x1 + x2) / 2) + ((x2 - x1) * (r1 ** 2 - r2 ** 2) / (2 * d * d)) + ((2 * area * (y1 - y2)) / (d * d))
    x0m = ((x1 + x2) / 2) + ((x2 - x1) * (r1 ** 2 - r2 ** 2) / (2 * d * d)) - ((2 * area * (y1 - y2)) / (d * d))
    y0p = ((y1 + y2) / 2) + ((y2 - y1) * (r1 ** 2 - r2 ** 2) / (2 * d * d)) + ((2 * area * (x1 - x2)) / (d * d))
    y0m = ((y1 + y2) / 2) + ((y2 - y1) * (r1 ** 2 - r2 ** 2) / (2 * d * d)) - ((2 * area * (x1 - x2)) / (d * d))
    return(x0p,x0m,y0p,y0m)

def earthquake_epicenter(x1, y1, t1, x2, y2, t2, x3, y3, t3):
    r1 = t1 * pWaveSpeed
    r2 = t2 * pWaveSpeed
    r3 = t3 * pWaveSpeed
    x0p1,x0m1,y0p1,y0m1 = center(x1, y1, r1, x2, y2, r2)
    x0p2,x0m2,y0p2,y0m2 = center(x1, y1, r1, x3, y3, r3)
    return whichEquals(x0p1,x0m1,x0p2,x0m2),whichEquals(y0p1,y0m1,y0p2,y0m2)
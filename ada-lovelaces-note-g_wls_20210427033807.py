from math import factorial
from fractions import Fraction

# Doesn't pass full tests :-(
# Suspect precission problem after n>20
# Speeded up via hashes (dict stores), first attemps were way sloooooow
# https://en.wikipedia.org/wiki/Bernoulli_number
# https://docs.python.org/3/library/fractions.html
# https://mathworld.wolfram.com/BernoulliNumber.html
# https://rosettacode.org/wiki/Bernoulli_numbers#Python:_Using_task_algorithm

COEF_STORE={}
F_STORE={}
B_STORE={}

def fact(n):
    try:
        return F_STORE[n]
    except KeyError:
        f=factorial(n)
        F_STORE[n]=f
        return f

def binCoef(n,k):
    try:
        return COEF_STORE[(n,k)]
    except KeyError:
        coef = fact(n) / (fact(k) * fact(n-k))
        COEF_STORE[(n,k)]=coef
        return coef

def B(n):
    try:
        return B_STORE[n]
    except KeyError:
        pass

    if (n%2)==1 and n>2:
        B_STORE[n]=0
        return 0

    if n==0:
        B_STORE[n] = 1
        return 1
    elif n==1:
        B_STORE[n] = -1/2
        return -1/2
    else:
        total=0
        for k in range(n):
            total += binCoef(n,k) * (B(k) / (n + 1 - k))
        B_STORE[n]=-total
        return -total

def bernoulli(n):
    F = Fraction(B(n)).limit_denominator(9999)
    return F.numerator,F.denominator

for i in range(100):
    print("{} {}".format(i,bernoulli(i)))
    
    from math import factorial
from fractions import Fraction as Fr
 
# The following code passes all tests, it's directly addapted from Rosseta Code, only change is B(1)'s sign
# https://rosettacode.org/wiki/Bernoulli_numbers#Python:_Using_task_algorithm
# def bernoulli(n):
#    if n==1:
#        return -1, 2
#    A = [0] * (n+1)
#    for m in range(n+1):
#        A[m] = Fr(1, m+1)
#        for j in range(m, 0, -1):
#          A[j-1] = j*(A[j-1] - A[j])
#    return A[0].numerator,A[0].denominator # (which is Bn)

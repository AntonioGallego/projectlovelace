def almost_pi(N):
    pi = 1
    for k in range(1,N):
        pi += (-1)**k / (2*k+1)
    return pi*4
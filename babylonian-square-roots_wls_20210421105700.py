def babylonian_sqrt(S):
    guess = S/2.0
    for i in range(50):
        if guess!=0:
            guess = (guess+(S/guess))/2
    return guess
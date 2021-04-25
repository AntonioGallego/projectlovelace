import numpy as np

## As the code suggests using mumpy, let's explore what it has to offer  
## x = [  5427,   5688,   6198,   6462,   6635,   7336,   7248,   7491,   8161,   8578,   9000]
## y = [18.079, 18.594, 19.753, 20.734, 20.831, 23.029, 23.597, 23.584, 22.525, 27.731, 29.449]
## print(np.corrcoef(x, y))
## [[1.         0.94684375]
## [0.94684375 1.        ]]

def correlation_coefficient(x, y):
    return (np.corrcoef(x, y)[0,1])
digits = {
    'black': 0,
    'brown': 1,
    'red': 2,
    'orange': 3,
    'yellow': 4,
    'green': 5,
    'blue': 6,
    'violet': 7,
    'grey': 8,
    'white': 9
}

multiplier = {
    'pink': 0.001,
    'silver': 0.01,
    'gold': 0.1,
    'black': 1,
    'brown': 10,
    'red': 100,
    'orange': 10 ** 3,
    'yellow': 10 ** 4,
    'green': 10 ** 5,
    'blue': 10 ** 6,
    'violet': 10 ** 7,
    'grey': 10 ** 8,
    'white': 10 ** 9
}

tolerance = {
    'none': 0.2,
    'silver': 0.1,
    'gold': 0.05,
    'brown': 0.01,
    'red': 0.02,
    'green': 0.005,
    'blue': 0.0025,
    'violet': 0.001,
    'grey': 0.0005
}


def resistance(band_colors):
    n_bands = len(band_colors)
    print(band_colors)
    if n_bands == 1:
        nominal_R = 0
        minimum_R = 0
        maximum_R = 0
    elif n_bands == 4:
        band1 = digits[band_colors[0]]
        band2 = digits[band_colors[1]]
        band3 = multiplier[band_colors[2]]
        band4 = tolerance[band_colors[3]]
        nominal_R=((10*band1)+band2)*band3
        tol = nominal_R * band4
        minimum_R = nominal_R - tol
        maximum_R = nominal_R + tol
    elif n_bands == 5:
        band1 = digits[band_colors[0]]
        band2 = digits[band_colors[1]]
        band3 = digits[band_colors[2]]      
        band4 = multiplier[band_colors[3]]
        band5 = tolerance[band_colors[4]]
        nominal_R=((100*band1)+(10*band2)+band3)*band4
        tol = nominal_R * band5
        minimum_R = nominal_R - tol
        maximum_R = nominal_R + tol
    return nominal_R, minimum_R, maximum_R
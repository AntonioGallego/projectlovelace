def rock_temperature(S, a, e):
    delta=5.670374419e-8
    T = (S*(1-a)/(4*e*delta))**0.25 # (^1/4 == fourth root of)
    return T-273.15 # Kelvin to Celsius
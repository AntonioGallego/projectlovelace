def exponential_growth(x0, k, dt, N):
    points=[x0]
    for i in range(N):
        last=points[-1]
        points.append(last + k*last*dt)
    return points

x0, k, dt, N = 5, 1, 0.6, 3
print(exponential_growth(x0, k, dt, N))
#[5, 8.0, 12.8, 20.48]

x0, k, dt, N = 1, 2.5, 0.1, 5
print(exponential_growth(x0, k, dt, N))
#[1, 1.25, 1.5625, 1.953125, 2.44140625, 3.0517578125]
def area_of_rectangles(rects, dx):
    total = 0
    for rec in rects:
        total += rec*dx
    return total
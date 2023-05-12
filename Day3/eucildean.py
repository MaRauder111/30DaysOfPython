import slope

slope_before = slope.y

print(slope_before)

x1 = 2
y1 = 2
x2 = 6
y2 = 10

slope = (y2-y1)/(x2-x1)

print(slope)

print(slope_before == slope)
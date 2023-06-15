def slope(x1,x2,y1,y2):
    # y = mx + c
    s = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
    y_intercept = lambda x1, y1, x2, y2: y1 - slope(x1, y1, x2, y2) * x1
    return y_intercept

x1 = 10
x2 = 20
y1 = 30
y2 = 40
print(slope(x1,x2,y1,y2))
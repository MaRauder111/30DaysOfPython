from random import randint

def rgb():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)

    return (r,g,b)

def rgb_array():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    rgb_arr = [r,g,b]
    return rgb_arr

def rgb_color_gen():
    r = str(randint(0, 255))
    g = str(randint(0, 255))
    b = str(randint(0, 255))
    return "rgb(" + r + "," + g + "," + b + ")"

# rgb()

# print(rgb_array())

# print(rgb_color_gen())
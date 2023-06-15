import random
from rgb import rgb

def generate_colors(string_value, int_value):
    if string_value == 'hexa':
        hexas = "1,2,3,4,5,6,7,8,9,0,a,b,c,d,e,f".split(",")
        hexCodes = []
        for i in range(int_value):
            hexCodes.append("#" + ''.join([random.choice(hexas) for _ in range(6)]))
        return hexCodes
    elif string_value == 'rgb':
        rgbs = []
        for _ in range(int_value):
            rgbs.append(rgb())
        return rgbs

print(generate_colors('hexa', 1))
print(generate_colors('rgb', 3))
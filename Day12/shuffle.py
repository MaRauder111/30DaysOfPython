import random

def shuffle_list(lst):
    return random.sample(lst, len(lst))

lst = [1,2,3,4,5,6,7,8,9,0]
print(shuffle_list(lst))
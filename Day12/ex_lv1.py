import random
import string

value = string.ascii_letters + string.digits

# print(value)

def random_user_id():
    ind = ' '
    for i in range(6):
        ind +=  random.choice(value)
    return ind

print(random_user_id())

# help(random)
def rand_user_id_input():
    charsize = int(input('Enter Character Size: '))
    charlimit = int(input('Enter how many user ids to generate: '))
    for _ in range(charlimit):
        identity = ''.join([random.choice(value) for _ in range(charsize)])
        print(identity)

rand_user_id_input()
def unique(lst):
    if len(set(lst)) == len(lst):
        return True
    else:
        return False

lst = [1,2,3,4,5,1]
print(unique(lst))
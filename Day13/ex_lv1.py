def list_comp(numbers):
    num = [i for i in numbers if i >= 1]
    return num

numbers = [-4, -3, -2, -1, 0, 1, 2, 4, 6]
print(list_comp(numbers))

def flatten(list_of_lists):
    return [x for sub in list_of_lists for sub2 in sub for x in sub2]

list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]

print(flatten(list_of_lists))

def lst_tuple():
    lst = []
    for i in range(11):
        lst.append((i,i**0,i**1,i**2,i**3,i**4))
    return lst

print(lst_tuple())
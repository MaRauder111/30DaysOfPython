# x = isinstance(3, int)

# print(x)

def same_data_type(lst):
    res = True
    for ele in lst:
        if not isinstance(ele, type(lst[0])):
            res = False
            break

    print(res)

lst = [1,2,3,4,5, 'Name']
lst1 = [12,3,5,6]
same_data_type(lst)
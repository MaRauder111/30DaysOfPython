def add_all_nums(*nums):
    list_nums = list(nums)
    print(list_nums)
    total = 0
    for i in list_nums:
        total += i
        print(i is type(int))
    return total

print(add_all_nums(10,20,30,40))
def calculate_mean(lst):
    length = len(lst)
    sum = 0
    for i in lst:
        sum += i
    mean = sum/length
    return mean


lst = [1,2,3,4,5]
print(calculate_mean(lst))
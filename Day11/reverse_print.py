def reverse_list(value):
    length = len(value)-1
    rev = []
    for i in range(length, -1, -1):
        rev.append(value[i])
    return rev

print(reverse_list([1,2,3,4,5]))
print(reverse_list(["A", "B", "C"]))
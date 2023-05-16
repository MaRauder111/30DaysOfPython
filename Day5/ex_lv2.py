ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages.sort()
print(ages)

min = ages[0]
last_idx = len(ages) - 1
max = ages[last_idx]

print(min, max)

ages.append(min)
ages.append(max)

print(ages)

middle_term = int(len(ages)/2)
print(middle_term)

ages.sort()
median = ages[middle_term]/2
print(median)

avg = sum(ages) / len(ages)
print(avg)

range = ages[last_idx] - sum(ages) / len(ages)
print(range)
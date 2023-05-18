it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add('Twitter')

print(it_companies)

it_companies.update(['TSP', 'Optum'])
print(it_companies)

it_companies.remove('IBM')
print(it_companies)

it_companies.discard('IBM')
print(it_companies)

print(A.union(B))
print(A.intersection(B))
print(A.issubset(B))
print(A.union(B))
print(B.union(A))
print(A.symmetric_difference(B))
del A
del B

ages = set(age)
print(ages)
print(f'Length of age {len(age)}\nLength of ages {len(ages)}')
print(len(ages) == len(age))

string = 'I am a teacher and I love to inspire and teach people'
print(string)

string = string.split()
print(string)
print(len(string))

string = set(string)

print(string)
print(len(string))
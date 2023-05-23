fruit = ['banana', 'orange', 'mango', 'lemon']
rev = list()
for i in range(3,-1,-1):
    rev.append(fruit[i])

print(rev)

for i in fruit:
    rev = [i] + rev
print(rev)
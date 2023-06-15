language = "Python"
lst = list(language)

print(type(lst))
print(lst)

lst = [i for i in language]
print(type(lst))
print(lst)

number = [i for i in range(11)]
print(number)

square = [i*i for i in range(11)]
print(square)

number = [(i, i*i) for i in range(11)]
print(number)

even = [i for i in range(100) if i%2 == 0]
print(even)
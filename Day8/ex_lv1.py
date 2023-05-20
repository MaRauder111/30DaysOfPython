dog = dict()

dog = {'name':'milo', 'color':'brown', 'breed': 'local', 'legs': 4, 'age':2}

print(dog)

student = {'first_name': 'Ningthoujam', 'last_name': 'Justwant', 'gender':'male', 'age':26, 'martial_status':'single', 'skills':['C', 'C++', 'Python', 'JS'], 'country':'India', 'address':'Palace Compound'}

print(student)
print(len(student))

print(type(student.get('skills')))
student['skills'].append('HTML')

print(student)
print(student.keys())
print(student.values())

student_lst = list(student.items())
print(student_lst)

student_lst.clear()
del student_lst
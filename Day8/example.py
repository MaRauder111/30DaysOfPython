empty = dict()
dic = {'key1' : ['value1' , 'value1_2'], 'key2' : 'value2'}

print(len(dic))
print(dic['key1'])


print(dic.get('key1'))

dic['key3'] = 'value3'
dic['key1'].append('value1_3')

print(dic)
print('key2' in dic)

dic.pop('key1')
print(dic)
dic.popitem()
print(dic)
# del dic

dic.items()
print(dic)
# dic.clear()
print(dic)

dic_cpy = dic.copy()

print(dic_cpy)
print(dic.keys())
print(dic.values())
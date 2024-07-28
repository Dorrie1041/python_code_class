# create the dict

dict1 = {'name': 'Dorrie', 'age': 34}
dict2 = dict([('name', 'zs'), ('age', 44)])

for key, value in dict2.items():
    print(key, value)

dict1['address'] = 'Wuhan'
print(dict1)

if 'age' in dict1:
    print(dict1['age'])

# dict1.clear()

# search
if 'address' in dict1:
    print(dict1['address'])

new_dict = dict.fromkeys(['name', 'age'])
print(new_dict)






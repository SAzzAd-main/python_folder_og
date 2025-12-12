# key value pair
# dictionary
# object
# hash table
# over lap with set

person ={'name': 'Kala pakhi', 'address': 'Kalipur', 'age': 23, 'job': 'bekar'}
print(person)
print(person['job'])
print(person.keys())
print(person.values())

# mutable
person['language'] = 'python'
person['name'] = 'sada pakhi'
del person['age']
print(person)

for key,value in person.items():
    print(key,':', value)

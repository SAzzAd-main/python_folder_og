def multiple():
    return 3, 4
print(multiple())

things = 'pen','tripod','water bottle','charger','phone','webcam','sunglass'
print(things)
print(type(things))
print(things[0])
print(things[2:5])
print(things[::-1])

# things[0] = 'brand'
# print(things[0])

print(len(things))

mega = ([2,3,5],[6,4,8,3])

# meaga [0] = 5 not acceptable
mega[0][1] = 999
print(mega)

if 'phone' in things:
    print('exist')

for item in things:
    print(item)
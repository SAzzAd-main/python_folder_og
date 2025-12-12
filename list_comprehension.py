numbers = [45, 87, 65, 43, 90, 85, 14, 26, 61, 70]
odds = []

for num in numbers:
    if num % 2 == 1 and num % 5 == 0:
        odds.append(num)
print(odds)

odd_nums = [num for num in numbers if num % 2 == 1 if num % 5 == 0]
print(odd_nums)

players = ['Sakib','Mushi','Tamim']
ages = [33,39,42]
age_comb = []

for player in players:
    for age in ages:
        age_comb.append([player,age])
print(age_comb)

age_comb2 = [[player,age] for player in players for age in ages]
print('Shortcut: ',age_comb2)

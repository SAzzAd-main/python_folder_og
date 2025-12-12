num = input('Enter your mark: ')

if int(num) >= 90:
    grade = 'A+'
elif int(num) >= 80:
    grade = 'A'
elif int(num) >= 70:
    grade = 'B+'
elif int(num) >= 60:
    grade = 'B'
elif int(num) >= 50:
    grade = 'C'
else:
    grade = 'F'

print('Your grade is: ',grade)
# args

def all_sum(num1,num2,*numbers):
    print(numbers)
    sum = num1 + num2
    for num in numbers:
        sum += num
        print(num, end = ' ')
    print('\n')
    return sum
total = all_sum(45,46,78,90,23,56)
print('all sum: ',total)
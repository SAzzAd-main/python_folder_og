
def a_lot(num1,num2):
    sum = num1 + num2
    multi = num1 * num2
    sub = num1 - num2
    # return [sum, multi, sub]
    return sum, multi, sub

num1 = int(input('Enter 1st number: '))
num2 = int(input('Enter 2nd number: '))
everything = a_lot(num1,num2)
print(everything)
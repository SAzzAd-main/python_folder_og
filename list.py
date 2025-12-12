# list, array, collection are same

# index =  0   1   2   3   4   5   6
numbers = [34, 54, 23, 10, 58, 74, 33]
# index =  -7  -6  -5   -4  -3  -2  -1

print(numbers[3],numbers[-3])

# list(star : end) start from the start index and stops before end index
print(numbers[2:5])

# list(start : end : step)
print(numbers[1:6:2])
print(numbers[5:0:-2])
print(numbers[3:])
print(numbers[:4])
print(numbers[:])  # shortcut to copy a list
print(numbers[::-1]) # shortcut to reverse a list
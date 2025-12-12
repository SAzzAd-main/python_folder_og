numbers = [34, 54, 23, 10, 58, 74, 33]
#  to add value at the end of a list

numbers[len(numbers):] = [91]
print(numbers[:])
numbers.append(55)
print(numbers[:])

# insert
numbers.insert(3,19)
print(numbers[:])

# remove
numbers.remove(10)
print(numbers[:])

# index return korbe
if 54 in numbers:
    index = numbers.index(54)
    print(index)

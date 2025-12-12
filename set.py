# list -> []
# tuple -> ()
#  set -> {}
#  set : unique items collection. no duplicate

numbers = [12,45,66,88,99,87,44,6,75,88,15,45,8]
print(numbers)

set_numbers = set(numbers)
print(set_numbers)

set_numbers.add(55)
print(set_numbers)

set_numbers.remove(6)
print(set_numbers)

if 9 in set_numbers:
    print("exist")
else:
    print("Not exist")

A = {1,3,5}
B = {1,2,3,4,5,6}

print(A & B)
print(A | B) # A U B
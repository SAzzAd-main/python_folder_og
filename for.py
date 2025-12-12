numbers = [5, 10, 15, 20, 25]
sum = 0
for num in numbers:
    sum += num
    if sum > 50:
        print("Sum exceeded 50, breaking the loop.")  
print(sum)

text = 'pagla hawar jole jole'
for char in text:
    if(char==' '):
        continue
    print(char)

# for i in range(1, 15, 2):
#     print(i)

# friends = ['abul', 'babul', 'cabul', 'dabul']

# for call in friends:
#     print(call)
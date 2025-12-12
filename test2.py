# a = [7, 0, 8, 0, 0, 9]
# b = ('gf','bf','cg','gf','bal')
# print(b.count('gf'))
# b[2] = 'gg'
# print(sum(a))

# a = {"key": "value",
#      "sazzad": "main",
#      "marks": "100",
#      "list": [1,2,0]
# }

# print(a.items())
# print(a.keys())

# set_prac = set()
# s1 = int(input("Enter a number: "))
# set_prac.add(s1)
# s2 = int(input("Enter a number: "))
# set_prac.add(s2)
# s3 = int(input("Enter a number: "))
# set_prac.add(s3)
# s4 = int(input("Enter a number: "))
# set_prac.add(s4)
# s5 = int(input("Enter a number: "))
# set_prac.add(s5)
# s6 = int(input("Enter a number: "))
# set_prac.add(s6)
# s7 = int(input("Enter a number: "))
# set_prac.add(s7)
# s8 = int(input("Enter a number: "))
# set_prac.add(s8)
# print(set_prac)

# s = set()
# s.add(20)
# s.add(20.5)
# s.add('20')

# print(len(s))

# s = {"valo": "Good",
#      "jao": "Go",
#      "bolo": "speak"
# }

# word = input("Enter a word: ")
# print(s[word])

# f = {}

# name = input("Enter name: ")
# lang = input("Enter language: ")
# f.update({name:lang})

# name = input("Enter name: ")
# lang = input("Enter language: ")
# f.update({name:lang})

# name = input("Enter name: ")
# lang = input("Enter language: ")
# f.update({name:lang})

# name = input("Enter name: ")
# lang = input("Enter language: ")
# f.update({name:lang})

# print(f)

# s = {8, 7, 12, "Harry", [1,2]}

# numbers = input("Enter numbers: ")
# n1str, n2str, n3str, n4str = numbers.split()
# num1 = int(n1str)
# num2 = int(n2str)
# num3 = int(n3str)
# num4 = int(n4str)

# summ = (num1+num2+num3+num4)/4

# if summ>40 and num1>33 and num2>33 and num3>33 and num4>33:
#     print("pass")
# else:
#     print("fail")

# l1 = ["sazzad","babu","fahim","bolla","galu"]
# if l1.find("sazzad")>-1:
#     print("Found")
# else:
#     print("Not found")

# l1 = "Make a lot of money"
# l2 = "buy now"
# l3 = "subscribe this"
# l4 = "click this"

# messege = input("Enter any message: ")

# if l1 in messege or l2 in messege or l3 in messege or l4 in messege:
#     print("Spam")
# else:
#     print("No")

# post = '''shuno er nam ki jno
#           vuila gasi
#            o mone porse harry'''
# if "harry" in post:
#     print("ache")
# else:
#     print("nai")

# l1 = [1,'badsha',45.05,33,21,False]

# for item in l1:
#     print(item,end=" ")


# for i in range(4):
#     print("printing")
#     if i == 2: # if i is 2, the iteration is skipped 
#         continue
#     print(i)

# num = int(input("Enter any number: "))
# for i in range(10,0):
#     print(num*i)



# num = int(input("Enter any number: "))
# fact = 1
# for i in range(1,(num+1)):
#     fact = fact * i
# print(fact)

# n = int(input("Enter n: "))

# for i in range(n):
#     j = 0
#     while j<=i:
#         print("*",end=" ")
#         j = j + 1
#     print()

# l = ["Harry", "Soham", "Sachin", "Rahul"]

# for name in l:
#     if name.startswith("S"):
#         print(f"Hello {name}")


# n = int(input("enter n: "))

# for i in range(1,n+1):
#     if i==1 or i==n:
#         print("*"* n,end="")
#     else:
#         print("*",end="")
#         print(" "* (n-2),end="")
#         print("*",end="")
#     print("")

# def convert(n):
#     if n==1:
#         return 1
#     # sum += n
#     return n+convert(n-1)

# c = float(input("Enter temparatue: "))
# f = convert(c)
# print(f)

# def pattern(n):
#     if n==0:
#         return
#     pattern(n-1)
#     print("*"*n,end="")
#     print()
# n = int(input("Enter n: "))
# pattern(n)

# def rem(l,w):
#     n = []
#     for item in l:
#         if item==w:
#             l.remove(w)
#         else:
#             n.append(item.strip(w))
#     print(l)
#     return n
# l = ["apnum","calcium","potacium","sodium","um"]
# word = input("Enter a word: ")
# print(rem(l,word))

m1 = 0
m2 = 0
a = "sazzad"
b = "sadi"
koto_point = 4

for i in range(5):
    man1 = input("Choose word: ")
    man2 = input("Choose word: ")

    if (man1=="snake" and man2=="water") or (man1=="water" and man2=="gun") or (man1=="gun" and man2=="snake"):
        m1 += 1
    elif (man1=="snake" and man2=="gun") or (man1=="water" and man2=="snake") or (man1=="gun" and man2=="water"):
        m2 += 1
if m1>m2:
    print(f"Winner is {a} and got points {m1}")
else:
    print(f"Winner is {b} and got points {m2}")
 
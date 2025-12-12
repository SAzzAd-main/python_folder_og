# স্ট্রিং কে খুবে সহজে slice করা যায়, যেমন 'I am Phitron' স্ট্রিং থেকে যদি আমরা 'Phitron' অংশটুকু পেতে চাই তাহলে myString[5:12] লিখলেই পেয়ে যএই কাজটি অবশ্য Backward বা নেগেটিভ ইনডেক্স ব্যবহার করেও করে দেখতে পারেনকিন্ত একটি কাজ কোনো ভাবেই করতে পারবে না , সেটি হলো স্ট্রিং এর কোনো ইলিমেন্ট চেঞ্জ করা। যেমন , myString[5]='T' লিখে রান করলে ইরোর খাবেন

# mystring = 'I am phitron'
# res = mystring.count('I')
# print(res)

# mytuple = (1,2,'hello',55,[1,2,3],(0,4))
# print(mytuple)

# print(mytuple.count(1))
# print(mytuple.index('hello'))

# myset = {2,3,4,1,2,3,7,1,5,3}
# yourset = {4,4,8,9,7,8,9,3}
# print(myset)
# myset.add(6)
# print(yourset)
# yourset.remove(9)
# ourset = myset | yourset
# print(ourset)

# my = {'name':'sazu','age':33,'course':('database','python','chemistry'),}

# for _,val in my.items():
#     print(val)

# print(my.keys())
# print(my.values())
# my['name'] = 'gafur'
# print(my['name'])

# from random import*
# print(random())
# # from randint import*
# print(randint(300,890)) 

# try:
#     x = int(input("Enter a number: "))
#     y = 10/x
#     print(y)
# except ZeroDivisionError:
#     print("zeror karone error hoise")
# except ValueError:
#     print("integer er jaigai onno value diacho")
# finally:
#     print('thank u code is over')

# with open("text.txt","w") as f:
#     f.write("la la ki ekta jani likhlam")
#     f.close()

# with open("text.txt","r") as f:
#     data = f.read()
#     print(data)

add = lambda a,b : a + b
print(add(4,5))

def apply(func,x):
    return func(x)
result = apply(lambda x : 10 + x, 5)
print(result)


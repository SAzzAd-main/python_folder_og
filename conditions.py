# in, not, not in, is, is not

a = 2
boss = True
if a > 5:
    print('a is greater')
    print('ki bujli')
elif a==3:
    print('paijjus')
else:
    print('parli nare parli na')


# if boss is True:
#     print('tel er baksho ni ashen')
# else:
#     print('lunch er pore ashen')

if boss is not True:
    print('lunch er pore ashen')
else:
    print('tel er baksho ni ashen')

# nested conditions

coin = 'head'

if boss==True:
    print('lunch er pore ashen')

    if coin=='tail':
        print('tail asche')
    else:
        print('head asche')

        if a>5 and 3%2==0:
            print('a is greater and 3 is even')
        elif a<5 or 3%2!=0:
            print('a is smaller or 3 is odd')
        else:
            print('kicho na') 
else:
    print('tel er baksho ni ashen')
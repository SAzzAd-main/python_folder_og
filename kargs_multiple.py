# def full_name(first, last):
#     nam = f"Full name is: {first} {last}"
#     return nam
# name = full_name(last='hossain',first='sazzad')
# print(name)


# kargs key wala argument. ig. key : arguement = 'title': 'mufti'

def famous_name(first,last,**title):
    nam = f"Full name is: {first} {last}"
    # print(title)
    # print(title['addition'])

    for ke,valu in title.items():
        print(ke,valu)
    return nam
    
name2 = famous_name(first='taher',last='ali',title='mufti',title2='hujur',addition='shakykh')
print(name2)
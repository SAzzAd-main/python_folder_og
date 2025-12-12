balance = 3000

def buy_things(item, price):
    # you can access global variable inside this function but you can't change it
    # nut to modify it you have to use 'global' keyword
    global balance 
    dream_phone = 'samsung' # local variable: it can't be accessed outside this function
    balance = balance - price
    print(f'balance after buying {item} is: {balance}')

buy_things('sunglass',200)
print(balance - 1000)
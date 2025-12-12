with open("Donkey.txt") as f:
    don = f.read()
content = don.replace("donkey","######")

with open("Donkey.txt","w")as f:
    f.write(content) 

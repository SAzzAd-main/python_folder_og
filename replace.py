with open("Donkey.txt") as f:
    content = f.read()
words = ["donkey","cow","onion"]

for word in words:
    content = content.replace(word,"#"*len(word))
with open("Donkey.txt","w") as f:
    f.write(content)
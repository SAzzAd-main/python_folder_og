def rem(l,w):
    n = []
    for item in l:
        if item==w:
            l.remove(w)
        else:
            n.append(item.strip(w))
    print(l)
    return n
l = ["apnum","calcium","potacium","sodium","um"]
word = input("Enter a word: ")
print(rem(l,word))
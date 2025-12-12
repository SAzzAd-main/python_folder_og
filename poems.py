with open("poems.txt") as f:
    l = f.read()
    if("twinkle" in l):
        print("The file contains \'twinkle\'")
    else:
        print("The file does not contain \'twinkle\'") 
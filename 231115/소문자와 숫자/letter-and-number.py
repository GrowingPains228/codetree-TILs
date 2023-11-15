string = input()

for elem in string :
    if elem.isdigit() :
        print(elem, end = "")
    elif elem.isalpha() :
        print(elem.lower(), end="")
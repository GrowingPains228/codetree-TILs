string = list(input())

for elem in string :
    if elem.isalpha() :
        print(elem.upper(), end = "")
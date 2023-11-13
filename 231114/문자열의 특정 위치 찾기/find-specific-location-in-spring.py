string, char = tuple(input().split())

if char not in string :
    print("No")
else :
    print(string.find(char))
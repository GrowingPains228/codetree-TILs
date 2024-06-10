n = int(input())

s = set()

for _ in range(n):
    string = input().split()

    if string[0] == "find":
        if int(string[1]) in s:
            print("true")
        else:
            print("false")
    elif string[0] == "add":
        s.add(int(string[1]))
    else :
        s.remove(int(string[1]))
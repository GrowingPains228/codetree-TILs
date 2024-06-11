from sortedcontainers import SortedSet
n = int(input())

s = SortedSet()

for _ in range(n):
    string = input().split()
    if string[0] == "add":
        s.add(int(string[1]))
    elif string[0] == "remove":
        s.remove(int(string[1]))
    elif string[0] == "find":
        print("true" if int(string[1]) in s else "false")
    elif string[0] == "lower_bound":
        key = s.bisect_left(int(string[1]))
        if key >= len(s):
            print("None")
        else:
            print(s[key])    
    elif string[0] == "upper_bound":
        key = s.bisect_right(int(string[1]))
        if key >= len(s):
            print("None")
        else:
            print(s[key])    
    elif string[0] == "largest":
        print(s[-1] if len(s) > 0 else "None")
    else:
        print(s[0] if len(s) > 0 else "None")
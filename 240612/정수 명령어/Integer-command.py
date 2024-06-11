from sortedcontainers import SortedSet

T = int(input())


def isEmpty(s):
    return len(s) == 0


for _ in range(T):
    k = int(input())
    s = SortedSet()
    for _ in range(k):
        string = input().split()

        if string[0] == 'I':
            s.add(int(string[1]))
        else:
            if isEmpty(s):
                continue

            if string[1] == '1':
                s.remove(s[-1])
            else:
                s.remove(s[0])
    
    if isEmpty(s):
        print("EMPTY")
    else:
        print(s[-1], s[0])
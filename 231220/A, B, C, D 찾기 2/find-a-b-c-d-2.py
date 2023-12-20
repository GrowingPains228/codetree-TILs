import sys

MAX_NUM = 40
arr = list(map(int, input().split()))
arr.sort()
for a in range(1, MAX_NUM + 1) :
    if a in arr:
        for b in range(1, MAX_NUM + 1) :
            if b in arr and a+b in arr :
                abcd = max(arr)
                for c in range(1, abcd - (a+b) + 1) :
                    if c in arr and a+c in arr and b+c in arr and a+b+c in arr :
                        d = abcd - (a+b+c)
                        print(a, b, c, d)
                        sys.exit()
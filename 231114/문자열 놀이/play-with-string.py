s,q = tuple(input().split())
s = list(s)
q = int(q)

for _ in range(q) :
    num, a, b = tuple(input().split())

    if int(num) == 1:
        a = int(a) 
        b = int(b)
        s[a-1], s[b-1] = s[b-1], s[a-1]
    else :
        for i in range(len(s)) :
            if s[i] == a :
                s[i] = b
        
    for elem in s :
        print(elem, end = "")
    print()
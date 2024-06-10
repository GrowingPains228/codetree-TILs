n, k = tuple(map(int, input().split()))

peoplelist = [set([i]) for i in range(1, n+1)]
pleyerlist = [ i for i in range(1, n+1) ]
arr = list()

for _ in range(k):
    a, b = tuple(map(int, input().split()))
    arr.append((a,b))

for i in range(3*k):
    a, b = arr[i % k]
    peoplelist[pleyerlist[a-1]-1].add(b)
    peoplelist[pleyerlist[b-1]-1].add(a)
    pleyerlist[a-1], pleyerlist[b-1] = pleyerlist[b-1], pleyerlist[a-1]

for elem in peoplelist :
    print(len(elem))
n, k = tuple(map(int, input().split()))

peoplelist = [set([i]) for i in range(1, n+1)]
arr = list()

for _ in range(k):
    a, b = tuple(map(int, input().split()))
    arr.append((a,b))

for i in range(3*k):
    a,b = arr[i % k]
    peoplelist[a-1].add(b)
    peoplelist[b-1].add(a)
    peoplelist[a-1], peoplelist[b-1] = peoplelist[b-1], peoplelist[a-1]

for elem in peoplelist:
    print(len(elem))
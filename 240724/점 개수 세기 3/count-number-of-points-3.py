n, q = map(int, input().split())
dots = list(map(int, input().split()))

d = dict()

for i in range(len(dots)):
    d[dots[i]] = i


for _ in range(q):
    dot1, dot2 = tuple(map(int, input().split()))
    print(d[dot2] - d[dot1] + 1)
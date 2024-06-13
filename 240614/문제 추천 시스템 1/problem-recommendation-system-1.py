from sortedcontainers import SortedSet
n = int(input())
problems = SortedSet()

for _ in range(n):
    P, L = tuple(map(int, input().split()))
    problems.add((L, P))

m = int(input())
for _ in range(m):
    inp = input().split()
    if inp[0] == "rc":
        idx = -1 if inp[1] == '1' else 0
        _, P = problems[idx]
        print(P)
    elif inp[0] == "ad":
        problems.add((int(inp[2]), int(inp[1])))
    else:
        idx = problems.bisect_left((int(inp[2]), int(inp[1])))
        if problems[idx] == (int(inp[2]), int(inp[1])):
            problems.remove((int(inp[2]), int(inp[1])))
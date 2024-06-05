from collections import defaultdict

n = int(input())
freqcit = defaultdict(lambda:0)
for _ in range(n):
    string = input()
    freqcit[string] += 1

ans = 0
for _, value in freqcit.items():
    ans = max(ans, value)

print(ans)
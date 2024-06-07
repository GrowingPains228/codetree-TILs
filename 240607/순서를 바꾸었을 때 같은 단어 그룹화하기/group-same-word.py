from collections import defaultdict

n = int(input())
dic = defaultdict(int)

for _ in range(n):
    inp = ''.join(sorted(input()))
    dic[inp] += 1

print(max(dic.values()))
from sortedcontainers import SortedDict

n = int(input())

sd = SortedDict()
for _ in range(n):
    string = input()

    if string in sd:
        sd[string] += 1
    else:
        sd[string] = 1

for key, value in sd.items():
    print(key, value)
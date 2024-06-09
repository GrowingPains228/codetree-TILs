from sortedcontainers import SortedDict

sd = SortedDict()

n = int(input())

for _ in range(n):
    string = input()
    if string in sd:
        sd[string] += 1
    else:
        sd[string] = 1


for key, value in sd.items():
    print(key, f"{value/n*100:.4f}")
n, m = tuple(map(int, input().split()))
d = dict()
d_num = dict()
for i in range(n):
    string = input()
    d[string] = i+1
    d_num[i+1] = string


for _ in range(m):
    command = input()
    if command in d:
        print(d[command])
    else:
        command = int(command)
        print(d_num[command])
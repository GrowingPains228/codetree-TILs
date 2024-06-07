n = int(input())
dic = dict()

for _ in range(n):
    inp = input()
    inp = sorted(inp)

    string = ""
    for elem in inp:
        string += elem
    
    if string in dic:
        dic[string] += 1
    else:
        dic[string] = 1

ans = 0
for value in dic.values():
    ans = max(ans, value)

print(ans)
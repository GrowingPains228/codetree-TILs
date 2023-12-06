string = list(input())
n = len(string)
cnt = 0
for i in range(n) :
    if string[i] != '(' :
        continue

    for j in range(i + 1, n) :
        if string[j] == ')' :
            cnt += 1
print(cnt)
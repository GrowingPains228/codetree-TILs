string = input()
n = len(string)

cnt = 0
for i in range(n-3) :
    if string[i:i+2] == '((' :
        for j in range(i + 2, n - 1) :
            if string[j:j+2] == '))' :
                cnt += 1

print(cnt)
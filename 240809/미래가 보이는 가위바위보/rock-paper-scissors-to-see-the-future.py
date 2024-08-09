n = int(input())

q = [input() for _ in range(n)]


L = [0] * n
R = [0] * n

for shape in "PHS":
    same_cnt = 0
    for i in range(n):
        if shape == q[i] :
            same_cnt += 1
        
        L[i] = max(L[i], same_cnt)

for shape in "PHS":
    same_cnt = 0
    for i in range(n-1, -1, -1):
        if shape == q[i]:
            same_cnt += 1

        R[i] = max(R[i], same_cnt)


ans = 0
for i in range(n-1):
    ans = max(ans, L[i] + R[i+1])

print(ans)
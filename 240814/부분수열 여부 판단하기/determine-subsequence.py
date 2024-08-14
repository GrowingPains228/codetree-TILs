n,m = map(int, input().split())
A = [0] + list(map(int, input().split()))
B = [0] + list(map(int, input().split()))

i = 1
ans = True
for j in range(1, m+1):
    while i <= n and A[i] != B[j]:
        i += 1
    
    if i == n+1:
        ans = False
        break
    else:
        i += 1


print("Yes" if ans else "No")
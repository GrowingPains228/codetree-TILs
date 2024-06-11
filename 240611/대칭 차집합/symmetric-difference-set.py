n1, n2 = tuple(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

s1 = set(A)
ans = n1 + n2

for elem in B:
    if elem in s1:
        ans -= 2

print(ans)
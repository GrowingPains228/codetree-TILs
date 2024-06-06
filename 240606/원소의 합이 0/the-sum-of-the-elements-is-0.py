n = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = list(map(int, input().split()))

dic_CD = dict()
for i in range(n):
    for j in range(n):
        if C[i] + D[j] in dic_CD:
            dic_CD[C[i] + D[j]] += 1
        else:
            dic_CD[C[i] + D[j]] = 1

ans = 0
for i in range(n):
    for j in range(n):
        sum_num = A[i] + B[j]

        diff = -sum_num

        if diff in dic_CD and dic_CD[diff] != 0:
            ans += dic_CD[diff]
            dic_CD[diff] = 0

print(ans)
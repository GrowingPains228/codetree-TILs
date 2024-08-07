import sys
n = int(input())

cpList = [tuple(map(int, input().split())) for _ in range(n)]
L_list = [0] * n
R_list = [0] * n

for i in range(1, n):
    x1,y1 = cpList[i-1]
    x2,y2 = cpList[i]
    L_list[i] = L_list[i-1] + abs(x2 - x1) + abs(y2 - y1)


for i in range(n-2, 1, -1):
    x1,y1 = cpList[i]
    x2,y2 = cpList[i+1]
    R_list[i] = R_list[i+1] + abs(x2 - x1) + abs(y2 - y1)

ans = sys.maxsize
for i in range(1, n-1):
    x1, y1 = cpList[i-1]
    x2, y2 = cpList[i+1]
    length = L_list[i-1] + R_list[i+1] + (abs(x2 - x1) + abs(y2 - y1))
    ans = min(ans, length)

print(ans)
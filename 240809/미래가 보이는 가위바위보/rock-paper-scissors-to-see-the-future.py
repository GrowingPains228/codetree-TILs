n = int(input())

q = [input() for _ in range(n)]

# 상대가 내는 가위 바위 보 리스트를 탐색하면서
# 연속으로 가장 많이 내는 유형을 L로 찾고
# 이후 오른쪽에서 부터 가장 믾이 내는 유형 R을 찾는다.
# 해당 구간이 만나는 N 을 기준으로
# LR 테크닉으로 최대 이긴 횟수를 찾는다.
# 0 : H(주먹), 1 : S(가위), 2 : P(보자기)
L = [[0] * (n+1) for _ in range(3)]
R = [[0] * (n+1) for _ in range(3)]

for i in range(1, n+1):
    if q[i-1] == 'H':
        L[0][i] = L[0][i-1] + 1
        L[1][i] = L[1][i-1]
        L[2][i] = L[2][i-1]
    elif q[i-1] == 'S':
        L[0][i] = L[0][i-1]
        L[1][i] = L[1][i-1] + 1
        L[2][i] = L[2][i-1]
    else:
        L[0][i] = L[0][i-1]
        L[1][i] = L[1][i-1]
        L[2][i] = L[2][i-1] + 1


for i in range(n-1, -1, -1):
    if q[i] == 'H':
        R[0][i] = R[0][i+1] + 1
        R[1][i] = R[1][i+1]
        R[2][i] = R[2][i+1]
    elif q[i] == 'S':
        R[0][i] = R[0][i+1]
        R[1][i] = R[1][i+1] + 1
        R[2][i] = R[2][i+1]
    else:
        R[0][i] = R[0][i+1]
        R[1][i] = R[1][i+1]
        R[2][i] = R[2][i+1] + 1

ans = 0
# k번째에 바꾼다고 가정.
for k in range(0, n+1):
    for i in range(3):
        result = L[i][k]
        
        for j in range(3):
            if i == j:
                continue
            
            ans = max(ans, result + R[j][k])

print(ans)
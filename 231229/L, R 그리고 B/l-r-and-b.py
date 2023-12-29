n = 10
board = [
    list(input())
    for _ in range(n)
]

L_x, L_y,B_x, B_y,R_x, R_y = 0,0,0,0,0,0
for i in range(n) :
    for j in range(n) :
        if board[i][j] == '.' :
            continue
        
        if board[i][j] == 'L' :
            L_y, L_x = i,j
        elif board[i][j] == 'B' :
            B_y, B_x = i,j
        else :
            R_y, R_x = i,j

# 만약 L과 B가 같은 라인(x축이든 y축에 위치한것)에 있고
# - 1. 그 사이에 R이 막고 있다면, 3 점이 추가된다.
# - 2. 그 사이에 R이 없다면, 최단거리를 구해주면됨.
ans = 0
if L_x == B_x :
    if R_y > min(L_y,B_y) and R_y < max(L_y,B_y) :
        ans = abs(B_y - L_y) + 1
    else :
        ans = abs(B_y - L_y) -1
elif  L_y == B_y :
    if R_x < max(L_x,B_x) and R_x > min(L_x,B_x) :   
        ans = abs(B_x - L_x) + 1
    else : 
        ans = abs(B_x - L_x) -1
# 같은 라인에 없는 경우라면, 두 좌표를 빼준 거리를 측정하면 된다.
else :
    ans = abs(B_y - L_y) + abs(B_x - L_x) -1

print(ans)
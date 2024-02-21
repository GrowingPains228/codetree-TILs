n,m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

def CostMining(x) :
    return x * x + (x+1) * (x+1)

# 먼저 총 황금의 개수를 세보는게 k 의 범위를 설정하는데 도움이 되지 않을까?
# 시간적 낭비일까?
cnt_gold = 0
for i in range(n) :
    for j in range(n) :
        if grid[i][j] == 0 :
            continue
        cnt_gold += 1

max_k = 0
Total_Gold_Cost = cnt_gold * m

# 손해가 절대 날 수 없는 k의 범위 
while CostMining(max_k) <= Total_Gold_Cost:
    max_k += 1

# k 거리안에 황금을 채굴할 수 있는 격자의 수를 세어보기
def draw_diamond_n_Count_Gold(x,y):
    cnt_gold = 0
    # 높이 양수 범위
    for dy in range(max_k) :
        for dx in range(-max_k + dy + 1, max_k - dy) :
            rx, ry = x + dx, y + dy
            if rx < 0 or rx >= n or ry >= n :
                continue
            if grid[ry][rx] == 0 :
                continue
            else :
                cnt_gold += 1

    #높이 음수 범위
    for dy in range(-max_k + 1, 0) :
        for dx in range(-max_k - dy + 1, max_k + dy) :
            rx, ry = x + dx, y + dy
            if rx < 0 or rx >= n or ry >= n or ry < 0 :
                continue
            if grid[ry][rx] == 0 :
                continue
            else :
                cnt_gold += 1
            
    return cnt_gold

ans = 0
for i in range(n) :
    for j in range(n) :
        ans = max(ans, draw_diamond_n_Count_Gold(j,i))

print(ans)
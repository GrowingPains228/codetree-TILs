n,m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 최악의 경우 k
max_k = 2*(n-1)

def cost_land(k) :
    return k * k + (k+1) * (k+1)


# 범위 안에 황금 찾아주기
def function(x,y,k) :
    cnt_gold = 0
    for i in range(n) :
        for j in range(n) :
            if abs(j-x) + abs(i-y) <= k :
                cnt_gold += grid[i][j]
    
    return cnt_gold

cnt_gold = 0
for i in range(n) :
    for j in range(n) :
        for k in range(max_k+1) :
            golds = function(j,i,k)

            if golds * m >= cost_land(k) :
                cnt_gold = max(cnt_gold, golds)

print(cnt_gold)
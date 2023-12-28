# 가위, 바위, 보
#   1    2    3
#   1    3    2
#   2    1    3
#   2    3    1
#   3    1    2
#   3    2    1

def RSP_game(type) :
    if type == 1:
        return (1, 2, 3)
    elif type == 2:
        return (1, 3, 2)
    elif type == 3:
        return (2, 1, 3)
    elif type == 4:
        return (2, 3, 1)
    elif type == 5:
        return (3, 1, 2)
    else :
        return (3, 2, 1)

n = int(input())
arr = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

RSP_arr = []
ans = 0
# 바위는 가위에 이기고, 보는 바위에 이기고, 가위는 보에 이긴다.
for i in range(6) :
    (scissors, rock, paper) = RSP_game(i)
    win = 0
    for d1, d2 in arr :
        if (d1, d2) in [(rock, scissors), (paper, rock), (scissors, paper)] :
            win += 1
    
    ans = max(ans, win)

print(ans)
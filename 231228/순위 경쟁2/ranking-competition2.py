n = int(input())
game_list = [
    tuple(input().split())
    for _ in range(n)
]

A,B = (0,0)
winner = 2 # 현재 명예에 정당
ans = 0
for person, score in game_list :
    if person == 'A' :
        A += int(score)
    else :
        B += int(score)

    win = 0
    if A == B :
        win = 2
    elif A > B :
        win = 0
    else : # A < B
        win = 1
    
    if winner != win :
        winner = win
        ans += 1

print(ans)
n = int(input())
A, B, C = 0,0,0

def who_winner() :
    if A > B and A > C :
        return 0
    elif A == B and A > C :
        return 1
    elif A == C and A > B :
        return 2
    elif A == B and B == C :
        return 3
    elif B > A and B > C :
        return 4
    elif A < B and B == C :
        return 5
    else : # C > A and C > B :
        return 6

win = 3
ans = 0
for _ in range(n) :
    man, score = tuple(input().split())
    if man == 'A' :
        A += int(score)
    elif man == 'B' :
        B += int(score)
    else :
        C += int(score)
    
    cur_winner = who_winner()
    if win != cur_winner :
        win = cur_winner
        ans += 1
    
print(ans)
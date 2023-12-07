import sys
n = 19
game_borad = [
    list(map(int, input().split())) for _ in range(n)
]

def in_range_right(x, y) :
    return y + 4 <= n

def in_range_down(x, y) :
    return x + 4 <= n

def in_range_rightdown(x, y) :
    return x + 4 <= n and y + 4 <= n

def in_range_rightUp(x,y) :
    return 0 <= x and y + 4 <= n

# 1 : 오른쪽 가로, 2 : 세로, 3 : 오른쪽 아래 대각선, 4: 왼쪽 아래 대각선, 으로 이김, -1 : 졌음
def is_win(x,y) :
    if in_range_right(x,y) and game_borad[x][y] == game_borad[x][y + 1] and game_borad[x][y+1] == game_borad[x][y + 2]  and game_borad[x][y+2] == game_borad[x][y + 3] and game_borad[x][y+3] == game_borad[x][y + 4] :
        return (True, 1)
    elif in_range_down(x,y) and game_borad[x][y] == game_borad[x+1][y] and game_borad[x+1][y] == game_borad[x+2][y]  and game_borad[x+2][y] == game_borad[x+3][y] and game_borad[x+3][y] == game_borad[x+4][y] :
        return (True, 2)
    elif  in_range_rightdown(x,y) and game_borad[x][y] == game_borad[x+1][y+1] and game_borad[x+1][y+1] == game_borad[x+2][y+2]  and game_borad[x+2][y+2] == game_borad[x+3][y+3] and game_borad[x+3][y+3] == game_borad[x+4][y+4] :
        return (True, 3)
    elif  in_range_rightUp(x,y) and game_borad[x][y] == game_borad[x-1][y+1] and game_borad[x-1][y+1] == game_borad[x-2][y+2]  and game_borad[x-2][y+2] == game_borad[x-3][y+3] and game_borad[x-3][y+3] == game_borad[x-4][y+4] :
        return (True, 4)
    
    return (False, -1)


win_x, win_y = 0,0
winner = 0

for i in range(n) :
    for j in range(n) :
        if game_borad[i][j] > 0 :
            Stone = game_borad[i][j]

            tf, wintype = is_win(i,j)

            if tf :
                winner = Stone
                print(winner)
                if wintype == 1 :
                    print(i+1, (j+1) + 2)
                elif wintype == 2 :
                    print((i+1)+2, (j+1))
                elif wintype == 3 : 
                    print((i+1)+2, (j+1)+2)
                else :
                    print((i+1)-2, (j+1)+2)
                
                sys.exit()
                break

    if winner != 0 :
        break


print(winner)
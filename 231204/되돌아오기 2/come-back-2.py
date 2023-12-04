commands = input()

dxs, dys = [0, 1,  0, -1],[1, 0, -1, 0 ]

dir_num = 0
x,y = 0,0
ans = -1
elapmed_cnt = 0
for command in commands :
    if command == 'F':
        x,y = x + dxs[dir_num], y + dys[dir_num]
    elif command == 'R' :
        dir_num = (dir_num + 1) % 4
    else :
        dir_num = (dir_num + 3) % 4
    
    elapmed_cnt += 1
    if x == 0 and y == 0 :
        ans = elapmed_cnt
        break
        
print(ans)
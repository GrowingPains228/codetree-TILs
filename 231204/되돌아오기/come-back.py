n = int(input())

dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]

direct_dict = {
    'N' : 0,
    'E' : 1, 
    'W' : 2,
    'S' : 3
}

x,y = 0, 0

return_time = -1
cnt_time = 0
for _ in range(n) :
    direct, distance = tuple(input().split())
    dic_num = direct_dict[direct]
    for _ in range(int(distance)) :
        x, y = x + dxs[dic_num], y + dys[dic_num]
        cnt_time += 1
        if x == 0 and y == 0 :
            return_time = cnt_time
            break

print(return_time)
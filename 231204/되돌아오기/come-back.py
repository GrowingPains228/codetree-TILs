n = int(input())

dxs, dys = [0, 1, -1, 0], [1, 0, 0, -1]

direct_dict = {
    'N' : 0,
    'E' : 1, 
    'W' : 2,
    'S' : 3
}

x,y = 0, 0

ans = -1
elapsed_time  = 0

def move(move_dir, dist) :
    global x,y
    global ans, elapsed_time

    for _ in range(dist) :
        x,y = x + dxs[move_dir], y + dys[move_dir]

        elapsed_time += 1

        if x == 0 and y == 0 :
            ans = elapsed_time
            return True
        
    return False

for _ in range(n) :
    s_dir, dist = tuple(input().split())
    dist = int(dist)

    move_dir = direct_dict[s_dir]

    done = move(move_dir, dist)

    if done :
        break

print(ans)
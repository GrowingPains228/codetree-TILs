MAX_RANGE = 100
arr = [''] * (MAX_RANGE + 1)
n = int(input())

for _ in range(n) :
    pos, value = tuple(input().split())
    arr[int(pos)] = value


max_size = 0
for i in range(MAX_RANGE + 1) :
    if arr[i] == '' :
        continue

    start_pos = i
    g_cnt, h_cnt = 0,0
    for j in range(i, MAX_RANGE + 1) :
        if arr[j] == 'G' :
            g_cnt += 1
        elif arr[j] == 'H' :
            h_cnt += 1
        else :
            continue
        
        if g_cnt == h_cnt :
            max_size = max(max_size, j-i)

print(max_size)
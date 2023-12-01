MAX_RANGE = 1000000
n,m = tuple(map(int, input().split()))

road_a = [0] * (MAX_RANGE + 1)
road_b = [0] * (MAX_RANGE + 1)

idx_a = 1
for _ in range(n) :
    verse, time = tuple(map(int, input().split()))
    distance = verse/time
    for _ in range(time) :
        road_a[idx_a] += distance
        idx_a += 1


idx_b = 1
for _ in range(m) :
    verse, time = tuple(map(int, input().split()))
    distance = verse/time
    for _ in range(time) :
        road_b[idx_b] += distance
        idx_b += 1

cnt = 0
for i in range(1, idx_a) :
    if road_a[i] > road_b[i] :
        if road_a[i - 1] < road_b[i - 1] :
            cnt += 1
            continue
    
    if road_a[i] < road_b[i] :
        if road_a[i - 1] > road_b[i - 1] :
            cnt += 1

print(cnt)
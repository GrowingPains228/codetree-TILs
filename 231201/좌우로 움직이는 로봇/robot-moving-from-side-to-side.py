MAX_DISTANCE = 1000000
n,m = tuple(map(int, input().split()))

road_a, road_b = [0] * (MAX_DISTANCE + 1), [0] * (MAX_DISTANCE + 1)

idx_a = 1
for _ in range(n) :
    t, d = tuple(input().split())
    distance = 1 if d == 'R' else -1
    for _ in range(int(t)) :    
        road_a[idx_a] = road_a[idx_a-1] + distance
        idx_a += 1

# 그 뒤의 모든 arr값을 현재 위치 값으로 세팅해준다.
for i in range(idx_a, MAX_DISTANCE + 1) :
    road_a[i] = road_a[i-1]
    
idx_b = 1
for _ in range(m) :
    t, d = tuple(input().split())
    distance = 1 if d == 'R' else -1
    for _ in range(int(t)) :    
        road_b[idx_b] = road_b[idx_b-1] + distance
        idx_b += 1

# 그 뒤의 모든 arr값을 현재 위치 값으로 세팅해준다.
for i in range(idx_b, MAX_DISTANCE + 1) :
    road_b[i] = road_b[i-1]

cnt = 0
for i in range(2, max(idx_a, idx_b)) :
    if road_a[i] == road_b[i] :
        if road_a[i-1] != road_b[i-1] :
            cnt += 1

print(cnt)
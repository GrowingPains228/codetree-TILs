MAX_RANGE = 1000000
n,m = tuple(map(int, input().split()))

road_a = [0] * (MAX_RANGE + 1)
road_b = [0] * (MAX_RANGE + 1)

# 시간과 속도에 따른 이동 거리를 배열에 기입한다.
idx_a = 1
for _ in range(n) :
    verse, time = tuple(map(int, input().split()))
    for _ in range(time) :
        road_a[idx_a] = road_a[idx_a - 1] + verse
        idx_a += 1

idx_b = 1
for _ in range(m) :
    verse, time = tuple(map(int, input().split()))
    for _ in range(time) :
        road_b[idx_b] = road_b[idx_b- 1] + verse
        idx_b += 1


#이동거리 배열을 비교하면서 선두가 몇번 바뀌었는지 체크한다.
cnt = 0
# 1은 a가 선두, 2는 b가 선두
leader = (1 if road_a[1] > road_b[1] else 2)
for i in range(2, idx_a) :
    if leader == 1 :
        if road_a[i] >= road_b[i] :
            continue

        leader = 2
        cnt += 1
    else :
        if road_a[i] <= road_b[i] :
            continue

        leader = 1
        cnt += 1

print(cnt)
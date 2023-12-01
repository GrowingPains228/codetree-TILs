MAX_time = 1000 * 1000
N,M = tuple(map(int, input().split()))
moved_legacy_a = [0] * (MAX_time + 1)
moved_legacy_b = [0] * (MAX_time + 1)

cur_idx_A = 1
for _ in range(N) :
    direction, time = tuple(input().split())
    time = int(time)

    while time :
        if direction == 'R' :
            moved_legacy_a[cur_idx_A] = moved_legacy_a[cur_idx_A - 1] + 1
        else :
            moved_legacy_a[cur_idx_A] = moved_legacy_a[cur_idx_A - 1] - 1

        cur_idx_A += 1
        time -= 1

cur_idx_B = 1
for _ in range(M) :
    direction, time = tuple(input().split())
    time = int(time)

    while time :
        if direction == 'R' :
            moved_legacy_b[cur_idx_B] = moved_legacy_b[cur_idx_B - 1] + 1
        else :
            moved_legacy_b[cur_idx_B] = moved_legacy_b[cur_idx_B - 1] - 1

        cur_idx_B += 1
        time -= 1

for i in range(1, MAX_time + 1) :
    if moved_legacy_a[i] == moved_legacy_b[i] :
        print(i)
        break
    
    if i == cur_idx_A :
        print(-1)
        break
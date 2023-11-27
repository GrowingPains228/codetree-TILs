OFF_SET = 1000
MAX_RANGE = 2000

n = int(input())
arr = [0] * (MAX_RANGE + 1)

moved = []
cur = 0
for _ in range(n) :
    x, direction = tuple(input().split())
    x = int(x)

    if direction == 'L' :
        start_point = cur - x
        end_point = cur
        cur -= x
    else :
        start_point = cur
        end_point = cur + x
        cur += x

    moved.append((start_point, end_point))

for start_p, end_p in moved :
    for i in range(start_p + OFF_SET, end_p + OFF_SET) :
        arr[i] += 1

cnt = 0
for elem in arr :
    if elem >= 2 :
        cnt += 1

print(cnt)
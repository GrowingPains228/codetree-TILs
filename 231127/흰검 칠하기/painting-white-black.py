OFFSET = 100000
MAX_RANGE = OFFSET * 2

n = int(input())

segment = []
arr = [0 for _ in range(MAX_RANGE + 1)]
blocks_w = [
    0 for _ in range(MAX_RANGE + 1)
]
blocks_b = [
    0 for _ in range(MAX_RANGE + 1)
]

cur = 0
for _ in range(n) :
    num, direction = tuple(input().split())
    num = int(num)

    if direction == 'L' :
        start_point = cur - num + 1
        end_point = cur + 1
        cur = cur - num + 1
        
    else :
        start_point = cur
        end_point = cur + num
        cur = cur + num - 1

    segment.append((start_point, end_point, direction))

for (start_point, end_point, direction) in segment :
    for i in range(start_point + OFFSET, end_point + OFFSET) :
        if direction == 'L' :
            blocks_w[i] += 1
            arr[i] = 1
        else :
            blocks_b[i] += 1
            arr[i] = 2
        
w = b = g = 0

for i in range(MAX_RANGE + 1) :
    if blocks_w[i] >= 2 and blocks_b[i] >= 2:
        g += 1
        continue
    
    if arr[i] == 1:
        w += 1
        continue
    
    if arr[i] == 2 :
        b += 1

print(w, b, g)
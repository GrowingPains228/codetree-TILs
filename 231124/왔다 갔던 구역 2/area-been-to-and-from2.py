OFFSET = 1000
MAX_R = 2000

#변수 선언 및 입력
n = int(input())
segments = []

current_idx = 0
for _ in range(n) :
    distance, direction = tuple(input().split())
    distance = int(distance)

    if direction == 'L' :
        start_po = current_idx - distance
        end_po = current_idx
        current_idx -= distance
    else :
        start_po = current_idx
        end_po = current_idx + distance
        current_idx += distance
    
    segments.append((start_po, end_po))

checked = [0] * (MAX_R + 1)

for x1, x2 in segments :
    #offset을 더해준다.
    x1, x2 = x1 + OFFSET, x2 + OFFSET

    #구간을 증감해준다.
    for i in range(x1, x2) :
        checked[i] += 1

cnt = 0
for elem in checked :
    if elem >= 2:
        cnt += 1
    
print(cnt)
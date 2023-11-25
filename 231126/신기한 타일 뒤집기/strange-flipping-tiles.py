# 앞선 문제에서 제시하는 해설처럼 해보기.
OFFSET = 100000


n = int(input())
a = [0] * (2*OFFSET + 1)
w,b = 0, 0

current_idx = OFFSET

for _ in range(n) :
    x, direction = tuple(input().split())
    x = int(x)

    # White로 바꿀때는 1, Black 으로 바꿀때는 2
    if direction == 'L' :
        while x > 0 :
            a[current_idx] = 1
            x -= 1

            if x : 
                current_idx -= 1
    else :
        while x > 0 :
            a[current_idx] = 2
            x -= 1

            if x :
                current_idx += 1


for elem in a :
    if elem == 1:
        w += 1
    elif elem == 2:
        b += 1
    
print(w, b)
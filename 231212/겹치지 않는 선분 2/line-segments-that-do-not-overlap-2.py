n = int(input())
segments = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
segments.sort(key=lambda x : x[0])

#만나게 되는 조건
# 1. 첫번째 점 보다 작은 값이라면, 두번째 점보다 큰 값이어야 한다.
# 2. 반대로, 첫번째 점 보다 큰 값이라면, 두번째 점보다 작은 값이야함
def is_meet(x1_1, x2_1, x1_2, x2_2) : 
    if x1_1 > x2_1 and x1_2 < x2_2 :
        return True

    if x1_1 < x2_1 and x1_2 > x2_2 :
        return True

    return False

cnt = 0
for i in range(n) :
    x1_1, x1_2 = segments[i]

    tf = True
    for j in range(n):
        if i == j :
            continue
        x2_1, x2_2 = segments[j]

        if is_meet(x1_1, x2_1, x1_2, x2_2) :
            tf = False
            break

    cnt += 1 if tf else 0

print(cnt)
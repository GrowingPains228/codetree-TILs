MAX_RANGE = 1000000
n,m = tuple(map(int , input().split()))

distance_arr_A = [0] * (MAX_RANGE + 1)
curIndex_A = 1
for _ in range(n) :
    v,t = tuple(map(int, input().split()))
    for _ in range(t) :
        distance_arr_A[curIndex_A] = distance_arr_A[curIndex_A - 1] + v
        curIndex_A += 1
    
distance_arr_B = [0] * (MAX_RANGE + 1)
curIndex_B = 1
for _ in range(m) :
    v,t = tuple(map(int, input().split()))
    for _ in range(t) :
        distance_arr_B[curIndex_B] = distance_arr_A[curIndex_B - 1] + v
        curIndex_B += 1

SCORE_STAGE = (True,True)
cnt = 0
for i in range(1, curIndex_A) :
    cur_RANK = (False, False)

    if distance_arr_A[i] == distance_arr_B[i] :
        cur_RANK = (True, True)
    elif distance_arr_A[i] > distance_arr_B[i] :
        cur_RANK = (True, False)
    else :
        cur_RANK = (False, True)

    if cur_RANK != SCORE_STAGE :
        cnt += 1
        SCORE_STAGE = cur_RANK

print(cnt)
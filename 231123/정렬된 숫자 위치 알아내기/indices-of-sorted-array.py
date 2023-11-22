n = int(input())
arr = list(map(int, input().split()))

order_arr = []
# 입력된 수열 값과 원래 있던 idx 값(과거의 idx)을 tuple로 만든 타입을 넣어준다.
for defore_idx in range(n) :
    order_arr.append((defore_idx,arr[defore_idx]))

# 입력된 값에 의해 정렬을 진행한다.
order_arr.sort(key=lambda x : x[1])

# 이동한 idx 의 값을 다시 새로운 tuple로 넣어준다.
arr = []
for idx_moved in range(n) :
    defore_idx, value = order_arr[idx_moved] # 언팩킹
    arr.append((idx_moved, defore_idx, value))

# defore_idx를 기준으로 오름차순 정렬 진행
arr.sort(key=lambda x : x[1])

#출력
for i in range(n) :
    idx_moved, _, _ = arr[i]
    print(idx_moved + 1, end = " ")
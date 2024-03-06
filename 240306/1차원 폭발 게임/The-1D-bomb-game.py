n,m = tuple(map(int, input().split()))
arr = [
    int(input()) for _ in range(n)
]
end_idx = n

def is_Continuous_elem():
    global arr
    for i in range(end_idx-1):
        if arr[i] == arr[i+1]:
            return True

    return False


def Bomb_and_copy(m):
    global arr, end_idx
    max_idx = len(arr)
    st = 0
    cnt = 1
    temp = []
    idx = 1
    while idx < end_idx:
        if arr[st] == arr[idx] :
            cnt += 1

            if idx == end_idx-1 and cnt >= m:
                for i in range(st, end_idx) :
                    arr[i] = 0
        else :
            if cnt >= m :
                for i in range(st, idx) :
                    arr[i] = 0
            st = idx
            cnt = 1

        idx += 1

    
    for i in range(end_idx):
        if arr[i] == 0 :
            continue
        temp.append(arr[i])
    end_idx = len(temp)

    for i in range(end_idx):
        arr[i] = temp[i]


while is_Continuous_elem() :
    Bomb_and_copy(m)

print(end_idx)
for i in range(end_idx):
    print(arr[i])
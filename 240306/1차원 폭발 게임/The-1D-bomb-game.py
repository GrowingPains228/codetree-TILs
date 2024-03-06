n,m = tuple(map(int, input().split()))
arr = [
    int(input()) for _ in range(n)
]
end_idx = n


def is_Continuous():
    global arr,end_idx,m

    if end_idx < m:
        return False

    ans = 1
    check_point = 0
    target = arr[check_point]
    cnt = 1
    for i in range(1, end_idx):
        if target == arr[i]:
            cnt += 1
            ans = max(ans, cnt)
        else:
            cnt = 1
            check_point = i
            target = arr[check_point]

    if ans >= m :
        return True
    return False


def Continuous_numbers():
    global arr, end_idx
    check_point = 0
    target = arr[check_point]
    cnt = 1
    for i in range(1, end_idx):
        if target == arr[i]:
            cnt += 1
        else:
            # 폭발할 애들 폭발
            if cnt >= m:
                Bomb(check_point, i)

            check_point = i
            target = arr[check_point]
            cnt = 1

    # 마지막 부분도 폭발할 애들이 있으면 0으로 채워주기
    if cnt >= m:
        Bomb(check_point, end_idx)


def Bomb(cp, ep):
    global arr
    for i in range(cp, ep):
        arr[i] = 0


def apply_gravity():
    global arr,end_idx
    temp = []
    for i in range(end_idx):
        if arr[i] != 0 :
            temp.append(arr[i])
    end_idx = len(temp)

    for i in range(end_idx):
        arr[i] = temp[i]
    

def simulation():
    Continuous_numbers()
    apply_gravity()


while is_Continuous():
    simulation()

print(end_idx)
for i in range(end_idx):
    print(arr[i])
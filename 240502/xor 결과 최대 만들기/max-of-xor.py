n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
value_arr = []
ans = -1


def cal_xor_value():
    result = value_arr[0]
    for i in range(1, m):
        result ^= value_arr[i]

    return result


def xor_Combination(curr_num, idx):
    global ans
    if curr_num == m+1:
        ans = max(ans, cal_xor_value())
        return

    for i in range(idx, n):
        target = arr[i]
        value_arr.append(target)
        xor_Combination(curr_num+1, i+1)
        value_arr.pop()


xor_Combination(1,0)
print(ans)
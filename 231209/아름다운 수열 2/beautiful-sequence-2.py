n,m = tuple(map(int, input().split()))
A_arr = list(map(int, input().split()))
B_arr = list(map(int, input().split()))

def is_beautiful(a_nums, b_nums) :
    length = len(a_nums)
    if length == 1 :
        if a_nums[0] == b_nums[0] :
            return True
        else :
            return False

    for i in range(length) :
        if a_nums[0] == b_nums[i] :
            return is_beautiful(a_nums[1:], b_nums[:i]+b_nums[i+1:])
            
    return False

cnt = 0
for i in range(n-m + 1) :
    if is_beautiful(A_arr[i : i+m], B_arr) :
        cnt += 1

print(cnt)
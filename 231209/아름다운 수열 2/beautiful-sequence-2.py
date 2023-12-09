n,m = tuple(map(int, input().split()))
A_arr = list(map(int, input().split()))
B_arr = list(map(int, input().split()))

group_b_retype = []

def get_combinations(nums) :
    if len(nums) == 0 :
        return [[]];

    result = []
    for i in range(len(nums)) :
        for comb in get_combinations(nums[:i] + nums[i + 1:]):
            result.append([nums[i]] + comb)
    
    return result

group_b_retype = get_combinations(B_arr)
    
cnt = 0
for i in range(n-2) :
    if A_arr[i : i+3] in group_b_retype :
        cnt += 1

print(cnt)
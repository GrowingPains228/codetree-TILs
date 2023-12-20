n, k = tuple(map(int, input().split()))
bridge = list(map(int, input().split()))

def is_possible_value(num) :
    possible_arr = []
    for i in range(n) :
        if bridge[i] <= num:
            possible_arr.append(i)
    
    length = len(possible_arr)
    for i in range(1, length) :
        if possible_arr[i] - possible_arr[i-1] > k :
            return False
    
    return True


ans = 101
for i in range(n, max(bridge[0], bridge[-1])-1, -1) :
    if is_possible_value(i) :
        ans = min(ans, i)

print(ans)
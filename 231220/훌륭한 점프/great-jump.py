MAX_NUM = 100
n, k = tuple(map(int, input().split()))
bridge = list(map(int, input().split()))

def is_possible_value(num) :
    last_idx = 0
    for i in range(1, n) :
        if bridge[i] <= num :
            if i - last_idx > k :
                return False
            last_idx = i
    return True


for i in range(max(bridge[0], bridge[-1]), MAX_NUM + 1) :
    if is_possible_value(i) :
        print(i)
        break
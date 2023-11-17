n,m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

def range_sum(a1, a2) :
    sum_value = 0
    for i in range(a1-1, a2) :
        sum_value += arr[i]

    return sum_value


for _ in range(m) :
    a1, a2 = tuple(map(int, input().split()))
    print(range_sum(a1, a2))
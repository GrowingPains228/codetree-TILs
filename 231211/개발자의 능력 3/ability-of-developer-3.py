import sys

MAX_VALUE = sys.maxsize
arr = list(map(int, input().split()))

def return_difference(n1, n2, n3) :
    part_sum = arr[n1] + arr[n2] + arr[n3] 
    dif_sum = sum(arr) - part_sum

    return abs(part_sum - dif_sum)

n = len(arr)
min_score = MAX_VALUE
for i in range(n) :
    for j in range(i + 1, n) :
        for k in range(j+1, n) :
            min_score = min(return_difference(i,j,k), min_score)
    
print(min_score)
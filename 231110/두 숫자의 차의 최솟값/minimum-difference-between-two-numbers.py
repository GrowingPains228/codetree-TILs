n = int(input())
arr = list(map(int, input().split()))

min_gap = 100
min_num = arr[0]

for i in range(1,n) :
    currrent_gap = arr[i] - min_num

    # 차이가 작으면 최소값 갱신
    if min_gap >= currrent_gap :
        min_num = arr[i]
        min_gap = currrent_gap

print(min_gap)
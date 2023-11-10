n = int(input())
arr = list(map(int, input().split()))

min_gap = 100

for i in range(1,n) :
    currrent_gap = arr[i] - arr[i-1]

    # 차이가 작으면 최소값 갱신
    if min_gap >= currrent_gap :
        min_gap = currrent_gap

print(min_gap)
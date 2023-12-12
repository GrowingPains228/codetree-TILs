n = int(input())

workers = [
    tuple(map(int, input().split()))
    for _ in range(n)
]
max_time = 0
for i in range(n) :
    times = [0] * 1001
    for j in range(n) :
        if i == j :
            continue

        start,end = workers[j]
        for k in range(start, end) :
            times[k] = 1

    max_time = max(max_time,sum(times))

print(max_time)
import math
n = int(input())
people = list(map(int, input().split()))
verse = list(map(int, input().split()))


def Get_time(position):
    time = 0
    for i in range(n):
        newTime = abs(position - people[i])/verse[i]
        time = max(time, newTime)
    return time


left, right = 1.0, 10**9
epsilon = 1e-7
while right - left > epsilon :
    mid1 = left + (right - left) / 3
    mid2 = right - (right - left) / 3

    time1 = Get_time(mid1)
    time2 = Get_time(mid2)

    if time1 > time2:
        left = mid1
    else:
        right = mid2

print(f"{Get_time((left + right)/2):.4f}")
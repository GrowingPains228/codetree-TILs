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
    mid = (left + right) / 2
    mid_left = (left + mid) / 2
    mid_right = (mid + right) / 2

    if Get_time(mid_left) > Get_time(mid_right):
        left = mid_left
    else:
        right = mid_right

print(f"{Get_time((left+right)/2):.4f}")
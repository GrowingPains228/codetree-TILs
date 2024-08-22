n = int(input())
MAX_RANGE = n * 2


def isPossible(target):
    if target%3 == 0 or target%5 == 0:
        return False

    return True


def CalculateNumOrder(target):
    return target - target//3 - target//5 + target//(3*5)


ans = 0
left, right = 1, MAX_RANGE
while left <= right:
    mid = (left + right)//2
    order = CalculateNumOrder(mid)
    if isPossible(mid) and order == n:
        ans = mid
        break

    if order >= n:
        right = mid - 1
    else:
        left = mid + 1


print(ans)
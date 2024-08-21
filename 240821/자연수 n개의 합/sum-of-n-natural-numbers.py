MAX_S = 10**18
s = int(input())


def sumRange(num):
    return num*(num+1)//2


def find_n(s):
    left, right = 1, s
    max_num = -1

    while left <= right:
        mid = (left + right)//2
        if sumRange(mid) <= s:
            max_num = max(max_num, mid)
            left = mid + 1
        else:
            right = mid - 1
    return max_num


print(find_n(s))
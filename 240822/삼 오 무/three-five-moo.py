import sys
INT_MAX = sys.maxsize

n = int(input())

def get_num_of_numbers(mid):
    # moo의 수를 세어준다.
    moo_cnt = mid//3 + mid//5 - mid//15

    # 전체 수(mid)에서 moo의 수를 배면
    # 서로 다른 수의 개수 == 몇번째 수
    return mid - moo_cnt

# 이 문제에서는
# [1~K]까지 적혀있는 서로 다른 수의 개수가
# N이상인 경우 중 가능한 K의 최솟값을 구하자
left = 1
right = INT_MAX
min_num = INT_MAX

while left <= right:
    mid = (left + right)//2
    if get_num_of_numbers(mid) >= n:
        right = mid - 1
        min_num = min(min_num, mid)
    else:
        left = mid + 1

print(min_num)
n = int(input())

# 숫자 입력 리스트
nums = [int(input()) for _ in range(n)]

# 누적 합 사용
prefix_sum = 0
remainder_map = {}
ans = 0

for i in range(n):
    prefix_sum += nums[i]
    remainder = prefix_sum%7
    if remainder in remainder_map:
        ans = max(ans, i - remainder_map[remainder])
    else:
        remainder_map[remainder] = i


print(ans)
import sys

n = int(input())
arr = list(map(int, input().split()))
total_score = sum(arr)
ans_arr = []
ans = sys.maxsize


# n 개만 골아서
# 전체 합계에서 n개만 뽑은 리스트의 합계를 뺀 값을 계산해주면 됨
def sum_all(curr_num, idx):
    global ans
    if curr_num == n:
        ans = min(ans, abs(total_score - 2 * sum(ans_arr)))
        return

    if idx >= 2*n:
        return

    ans_arr.append(arr[idx])
    sum_all(curr_num + 1, idx + 1)
    ans_arr.pop()
    sum_all(curr_num, idx + 1)


sum_all(0, 0)
print(ans)
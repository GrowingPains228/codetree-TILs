n = int(input())
arr = list(map(int, input().split()))
sort_arr = sorted(arr)

# 3.모든 수가 모두 0 이하면 0 이 가장 큰 수이므로, 0 을 출력해주고 종료 그게 아니라면 다음 넘어가기
ans = 0
max_num = sort_arr[-1]
if max_num == 0  :
    pass
elif max_num < 0 :
    ans = sort_arr[-1] * sort_arr[-2] * sort_arr[-3]
else :
    for i in range(n) :
        for j in range(i + 1, n) :
            for k in range(j + 1, n) :
                ans = max(ans, arr[i] * arr[j] * arr[k])

print(ans)
n = int(input())
arr = list(input().split())
ans = 0

# 'A' 부터 알파벳 순서대로 찾아 가장 앞으로 이동합니다.
for i in range(n) :
    x = chr(ord('A') + i)

    # i번째 알파벳을 찾아 idx에 저장
    idx = 0
    for j in range(n) :
        if arr[j] == x :
            idx = j
            break
    
    # idx번째 알파벳을 i번째 위치까지 swap한다.
    for j in range(idx-1, i-1, -1) :
        arr[j], arr[j+1] = arr[j+1], arr[j]
        ans += 1
    
print(ans)
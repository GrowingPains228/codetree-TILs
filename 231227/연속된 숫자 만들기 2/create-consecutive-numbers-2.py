arr = list(map(int, input().split()))

ans = 0
# 1. 바로 입력된 숫자들이 전부 연속된다면
if arr[0] + 2 == arr[2] :
    pass
else : 
    if arr[0] + 2 == arr[1] or arr[1] + 2 == arr[2] : 
        ans = 1
    else :
        ans = 2

print(ans)
n = int(input())
arr = [
    int(input()) for _ in range(n)
]

#평균을 구해서 평균이 될때까지 다른 곳으로 옮기면 됨.
avg = int(sum(arr)/len(arr))

ans = 0
for elem in arr :
    if elem > avg :
        ans += elem - avg
print(ans)
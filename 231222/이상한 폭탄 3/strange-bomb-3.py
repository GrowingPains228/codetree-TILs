MAX_NUM = 1000000

booms = [0] * (MAX_NUM + 1)
n, k = tuple(map(int, input().split()))
arr = [
    int(input()) for _ in range(n)
]


def is_range(num) :
    return 0 <= num and num < n


for i in range(n) :
    boom_num = arr[i]
    for j in range(i-k, i+k+1) :
        # 같은 위치라면 패스
        if i == j :
            continue

        # 같은 숫자를 가진 폭탄이 있으면, 터짐
        # 바로 for문 빠져 나오기
        if is_range(j) and arr[j] == boom_num :
            booms[boom_num] += 1
            break
    
ans = 0
for i in range(MAX_NUM+1) :
    if booms[i] == 0 :
        continue

    if booms[i] >= booms[ans] :
        ans = i

print(ans)
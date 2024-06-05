n, k = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

# 시간 복잡도 n**2 이하로 끝내기.
count = dict()
for elem in arr:
    if elem in count:
        count[elem] += 1
    else:
        count[elem] = 1

diff_index = []

ans = 0
for elem1 in arr:
    count[elem1] -= 1
    diff  = k - elem1
    for elem2 in arr:
        if count[elem2] <= 0:
            continue
        count[elem2] -= 1
        diff_index.append(elem2)
        if (diff - elem2) in count and count[diff - elem2] > 0 :
            ans += count[diff - elem2]
    
    while len(diff_index) > 0:
        count[diff_index.pop()] += 1

print(ans)
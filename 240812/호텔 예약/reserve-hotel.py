n = int(input())

arr = [tuple(map(int, input().split())) for _ in range(n)]

segments = list()
for i, (a, b) in enumerate(arr):
    segments.append((a, -i, 1))
    segments.append((b, -i, -1))

segments.sort(key=lambda x : (x[0], x[1])) # 시간 순으로 정렬을 하되, 시간이 똑같으면 좀 더 뒷 순번의 idx가 앞으로 오게 만든다.

ans = 0
cnt = 0
for (x, idx, v) in segments:
    if v == 1:
        cnt += 1
        ans = max(ans, cnt)
    else:
        cnt -= 1

print(ans)
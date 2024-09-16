n = int(input())
lessons = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

lessons.sort(key = lambda x : x[1])
ans = 0
curEndTime = 0
for (s,e) in lessons:
    if curEndTime > s:
        continue
    
    ans += 1
    curEndTime = e

print(ans)
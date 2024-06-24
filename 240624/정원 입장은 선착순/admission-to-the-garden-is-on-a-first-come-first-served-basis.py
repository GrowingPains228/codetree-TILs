import heapq

n = int(input())
pq = []

# 도착 시간에 우선순위를 둔 큐를 튜플형태로 넣고
for i in range(1, n+1):
    arriveTime, time = tuple(map(int, input().split()))
    heapq.heappush(pq, (arriveTime, i, time))

ans = 0
currTime = 0
a, _, t = heapq.heappop(pq) # 일단 처음 한 사람 꺼내서 정원 구경하게 하기
currTime = a + t        # 정원 구경하고 난 시간 계산해주기
wait_group = []

# 계산
while pq:
    arri_time, idx, tt = pq[0]
    if currTime <= arri_time:
        heapq.heappop(pq)
        currTime = arri_time
    else:
        heapq.heappop(pq)
        heapq.heappush( wait_group, (idx, arri_time, tt))
        while pq :
            a, i, t = pq[0]
            if currTime > a :
                heapq.heappop(pq)
                heapq.heappush( wait_group, (i, a, t))
            else:
                break

        _, arri_time, tt = heapq.heappop(wait_group)

        ans = max(ans, currTime - arri_time) # 기다린 시간 기록해주기

        while wait_group:
            idxxx, aaa, ttt = heapq.heappop(wait_group)
            heapq.heappush( pq, (aaa, idxxx, ttt))

    # 들어간 사람이 다 구경하고 나온 시간 체크.
    currTime += tt

print(ans)
n, m = tuple(map(int, input().split()))
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
ans = 0
for _ in range(m):
    start,end = tuple(map(int, input().split()))
    graph[start].append(end)
    graph[end].append(start)


def dfs(vertex):
    global ans
    for neighbor in graph[vertex]:
        if not visited[neighbor]:
            ans += 1
            visited[neighbor] = True
            dfs(neighbor)


visited[1] = True
dfs(1)
print(ans)
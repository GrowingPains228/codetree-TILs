import sys
n, m = tuple(map(int, input().split()))
dot_list = list()
select_list = list()
for _ in range(n):
    x,y = tuple(map(int, input().split()))
    dot_list.append((x,y))
ans = sys.maxsize


def Get_Distance():
    dist = 0

    for i in range(m-1):
        x1, y1 = select_list[i]
        for j in range(i+1, m):
            x2, y2 = select_list[j]

            dist = max(dist, (x1-x2)**2 + (y1-y2)**2)

    return dist


def find_max_dist(curr_idx, cnt):
    global ans, select_list
    if curr_idx == n:
        if cnt == m:
            ans = min(ans, Get_Distance())
        return

    # 골랐을때
    select_list.append(dot_list[curr_idx])
    find_max_dist(curr_idx+1, cnt +1)
    select_list.pop()

    # 안골랐을때
    find_max_dist(curr_idx+1, cnt)


find_max_dist(0,0)
print(int(ans))
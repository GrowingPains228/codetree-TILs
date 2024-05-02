import sys
n, m = tuple(map(int, input().split()))
dot_list= list()
select_list = list()
for _ in range(n):
    x,y = tuple(map(int, input().split()))
    dot_list.append((x,y))
ans = sys.maxsize


def max_dist():
    # (0,0)에서 가장 가깝고 가장 먼 점을 선택하면 된다.
    min_dot, max_dot = (100,100),(1, 1)
    min_dist, max_dist = (100**2 + 100**2), 2

    for (x,y) in select_list:
        dist = x**2 + y**2
        if min_dist > dist :
            min_dot = (x,y)
            min_dist = dist

        if max_dist < dist :
            max_dot = (x,y)
            max_dist = dist

    return Cal_distance(min_dot, max_dot)


def Cal_distance(dot1, dot2):
    (x1, y1), (x2, y2) = dot1, dot2
    return ((x1-x2)**2 + (y1-y2)**2)**(1/2)


def find_max_dist(curr_idx, cnt):
    global ans
    if curr_idx == n:
        if cnt == m:
            ans = min(ans, max_dist())
        return

    # 골랐을때
    select_list.append(dot_list[curr_idx])
    find_max_dist(curr_idx + 1, cnt + 1)
    select_list.pop()

    # 안골랐을때
    find_max_dist(curr_idx + 1, cnt)


find_max_dist(0,0)
print(int(ans**2))
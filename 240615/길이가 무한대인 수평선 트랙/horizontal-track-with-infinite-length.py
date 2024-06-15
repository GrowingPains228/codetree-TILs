from sortedcontainers import SortedSet

n, t = tuple(map(int, input().split()))
p, v = list(), list()


for _ in range(n):
    x, velocity = tuple(map(int, input().split()))
    p.append(x)
    v.append(velocity)

people_p = SortedSet()
events = SortedSet()


def add_event(p1, v1, p2, v2):
    if v1 <= v2:
        return

    events.add(((p2-p1)/(v1-v2), p1, v1))


def remove_event(p1, v1, p2, v2):
    if v1 <= v2:
        return

    events.remove(((p2-p1)/(v1-v2), p1, v1))


for i in range(n):
    people_p.add((p[i], v[i]))

for i in range(n-1):
    add_event(p[i], v[i], p[i+1], v[i+1])

while events:
    curr_t, x, velocity = events[0]

    if curr_t > t:
        break
    
    people_p.remove((x,velocity))
    events.remove((curr_t, x, velocity))

    index = people_p.bisect_right((x,velocity))
    np, nv = people_p[index]

    # 바로 뒤에 사람이 있다면
    # 사람의 정보를 가져와서
    # 업데이트 해준다.
    if index != 0:
        index -= 1
        px, pv = people_p[index]
        remove_event(px, pv, x, velocity)
        add_event(px, pv, np, nv)
    
print(len(people_p))
n, g = tuple(map(int, input().split()))
group = [
    list(map(int, input().split()))
    for _ in range(g)
]
group_len = [(i, group[i][0]) for i in range(g)]
group_len.sort(key = lambda x: x[1])

s = set() #초대장을 받은 사람들 Hashset
ans = 0

# 1번 사람들에게는 무조건 초대장을 준다.
for i in range(g):
    s.add(group[i][1])
    if group[i][0] == 2:
        s.add(group[i][2])


def is_set_element(index, length):
    cnt = 2
    notin_element = []

    for i in range(3, length+1): # 제일 마지막 전까지 초대받은 그룹인지 아닌지 체크
        if group[index][i] in s:
            cnt += 1
        else:
            notin_element.append(group[index][i])

    if cnt+1 == length:
        s.add(notin_element.pop())


for (index, length) in group_len:
    if length < 3:
        continue

    is_set_element(index, length)

print(len(s))
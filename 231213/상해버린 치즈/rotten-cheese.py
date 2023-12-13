# n : 사람의 수
# m : 치즈의 수
# d : 치즈를 먹은 기록의 수
# s : 아픈 기록의 수
n,m,d,s = tuple(map(int, input().split()))
cheese = [0] * m
people = [False] * n

eat_notes = [
    tuple(map(int, input().split()))
    for _ in range(d)
]

pain_notes = [
    tuple(map(int, input().split()))
    for _ in range(s)
]

for i in range(s) :
    person, time = pain_notes[i]
    for (who, what, when) in eat_notes :
        if person == who :
            if when < time :
                cheese[what-1] += 1 # 상했을 가능성이 있는 치즈에 가중치를 준다
            # else :
            #     cheese[what-1] -= 1 # 상했을 가능성이 없는 치즈라 판단, 가중치 감소

# 상한 치즈에 대한 가중치는 아픈 기록수와 같은 치즈에 대해서 가장 의심하면 된다.
for i in range(m) :
    # 상한 치즈를 먹은 사람들 업데이트
    if cheese[i] >= s :
        for (who, what, when) in eat_notes :
            if (i + 1) == what :
                people[who-1] = True

ans = sum(people)
print(ans)
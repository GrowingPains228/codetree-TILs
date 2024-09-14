n = int(input())
x_people = list(map(int, input().split()))
v_people = list(map(int, input().split()))


def is_Possible(time) :
    max_x = x_people[0] - time * v_people[0]
    min_x = x_people[0] + time * v_people[0]

    for i in range(1, n):
        max_x = max(max_x, x_people[i] - time * v_people[i])
        min_x = min(min_x, x_people[i] + time * v_people[i])
    
    return max_x <= min_x


left, right = 0, 1e10
ans = 1e10

for _ in range(100):
    mid = (left + right) / 2
    
    if is_Possible(mid):
        ans = min(ans, mid)
        right = mid
    else :
        left  = mid
    
print(f"{ans:0.4f}")
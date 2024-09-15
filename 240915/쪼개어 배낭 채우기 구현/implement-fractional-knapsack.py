n, m = map(int, input().split())
value_list = list()
weight = 0
ans_value = 0

# 세팅
for i in range(n):
    w, v = map(int, input().split())
    value_list.append((v/w, w, v))

value_list.sort(reverse=True)

for i in range(n):
    (value, w, v) = value_list[i]
    if weight + w > m:
        ans_value += value * (m - weight)
        break
    else:
        weight += w
        ans_value += v

print(f"{ans_value:0.3f}")
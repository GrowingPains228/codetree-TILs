MAX_X = 1000000
n, k = map(int, input().split())

line_list = [0] * (MAX_X+1)
input_Max_x = 0
for _ in range(n):
    value, x = map(int, input().split())
    line_list[x] += value
    input_Max_x = max(input_Max_x, x)

j = 0
ans = 0
sum_val = 0
for i in range(input_Max_x+1):
    while j+1 <= input_Max_x and j <= i + 2*k:
        sum_val += line_list[j]
        j += 1

    ans = max(ans, sum_val)
    sum_val -= line_list[i]

print(ans)
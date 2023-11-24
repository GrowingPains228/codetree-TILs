OFFSET = 100

n = int(input())

lines = [0] + [ 0 for _ in range(0, 100 + OFFSET + 1)]
input_lines = [
    tuple(map(int, input().split())) for _ in range(n)
] 

for (x1,x2) in input_lines :
    for i in range(x1 + OFFSET, x2 + OFFSET) :
        lines[i] += 1

# 최대값이 있는 위치를 선별한다.
print(max(lines))
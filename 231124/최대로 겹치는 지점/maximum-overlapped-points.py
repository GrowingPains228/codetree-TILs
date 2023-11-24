Max_value = 100
n = int(input())
lines = [0] * (Max_value + 1)
segment = [
    tuple(map(int, input().split())) for _ in range(n)
] 

for (x1, x2) in segment :
    for i in range(x1, x2 + 1) :
        lines[i] += 1
    
print(max(lines))
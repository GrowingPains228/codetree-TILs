arr = [ list(map(int, input().split())) for _ in range(4) ]

sum_num = 0
for i in range(4) : 
    sum_num += sum(arr[i][:i+1:])

print(sum_num)
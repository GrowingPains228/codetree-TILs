n = int(input())

sum_int = 0
for _ in range(n) :
    user_input = int(input())
    sum_int += user_input

sum_int = str(sum_int)
print(sum_int[1:] + sum_int[0])
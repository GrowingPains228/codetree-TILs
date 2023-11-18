N = int(input())
cnt = 0

def count_AddFunction(number) :
    global cnt
    if number == 1:
        return 1
    
    cnt += 1
    return count_AddFunction(number//2) if number%2 == 0 else count_AddFunction(number//3)

count_AddFunction(N)
print(cnt)
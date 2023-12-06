# carry 판별 함수
def is_carry(num1, num2, num3) :
    while num1 != 0 or num2 != 0 or num3 != 0 :
        if num1%10 + num2%10 + num3%10 >= 10 :
            return True
        
        num1, num2, num3 = num1//10, num2//10, num3//10

    return False


n = int(input())
arr = [ int(input()) for _ in range(n)]

ans = -1
for i in range(n-2) :
    for j in range(i+1, n -1) :
        for k in range(j+1, n) :
            if not is_carry(arr[i],arr[j], arr[k]) :
                ans = max(sum([arr[i], arr[j], arr[k]]), ans)

print(ans)
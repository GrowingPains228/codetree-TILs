n = int(input())
arr = list(map(int, input().split()))

def LCM(arr) :
    tf = False
    commpn_int = 1
    for i in range(2,max(arr) + 1) :
        for j in range(n) :
            if arr[j] % i == 0 :
                arr[j] //= i 
                tf = True
        if tf :
            commpn_int = i
            break
            
    if tf :
        return LCM(arr) * commpn_int
    else :
        return 1

print(LCM(arr))
n = int(input())
arr = list(map(int, input().split()))

def find_max(n) :
    if n == 0 :
        return arr[0]
    
    return arr[n-1] if arr[n-1] > find_max(n-1) else find_max(n-1)

print(find_max(n))
n = int(input())
arr = list(map(int, input().split()))

def find_max(n) :
    if n <= 0 :
        return arr[0]
    
    return max(find_max(n-1), arr[n])

print(find_max(n-1))
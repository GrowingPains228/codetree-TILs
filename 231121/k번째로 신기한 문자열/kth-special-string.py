n, k, T = tuple(input().split())
n = int(n)
k = int(k)

arr = [
    input() for _ in range(n)
]

def check_str(parent_str, child_str) :
    length = len(child_str)

    if parent_str[:length] == child_str :
        return True
    else : 
        return False

arr.sort()

for elem in arr :
    if check_str(elem, T) is False :
        arr.remove(elem)

print(arr[k-1])
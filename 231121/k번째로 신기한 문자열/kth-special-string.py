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
count = 0
for i in range(n) :

    if check_str(arr[i], T) is False :
        continue

    count += 1

    if count == k :
        print(arr[i])
from sortedcontainers import SortedSet
n, m = tuple(map(int, input().split()))
arr = SortedSet(list(map(int, input().split())))
m_list = list(map(int, input().split()))

for elem in m_list:
    target = arr.bisect_left(elem)
    if target == len(arr) or target == 0: # 없는 경우
        print(-1)
        continue
    
    if arr[target] > elem:
        target -= 1

    print(arr[target])
    arr.remove(arr[target])
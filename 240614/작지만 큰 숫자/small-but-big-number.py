from sortedcontainers import SortedSet
n, m = tuple(map(int, input().split()))
arr = SortedSet(list(map(int, input().split())))
m_list = list(map(int, input().split()))

for elem in m_list:
    target = arr.bisect_right(elem)
    
    if target == 0 :
        print(-1)
        continue

    print(arr[target-1])
    arr.remove(arr[target-1])
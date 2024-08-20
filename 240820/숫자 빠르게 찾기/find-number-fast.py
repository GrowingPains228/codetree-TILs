# Hashmap으로 풀면 정말 빠르지만, 문제에서 풀라고 했던 "이진 탐색"으로 풀자!
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arrDict = dict()
for i in range(n):
    arrDict[arr[i]] = i+1


def find_target_by_Hashmap(target):
    return arrDict.get(target, -1)


for _ in range(m):
    num = int(input())
    order = find_target_by_Hashmap(num)
    print(order)
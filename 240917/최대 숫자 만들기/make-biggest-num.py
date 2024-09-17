from functools import cmp_to_key

# custom comparator 사용하기
def compare(x, y):
    if str(x) + str(y) > str(y) + str(x):
        return -1
    elif str(x) + str(y) < str(y) + str(x):
        return 1
    else:
        return 0


n = int(input())
group = [
    int(input()) for _ in range(n)
]

group.sort(key = cmp_to_key(compare))

for elem in group:
    print(elem, end = '')
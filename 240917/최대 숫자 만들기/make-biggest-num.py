from functools import cmp_to_key

# custom comparator 사용하기
def compare(x, y):
    result1 = x + y
    result2 = y + x
    result1 = int(result1)
    result2 = int(result2)

    if result1 > result2:
        return -1
    elif result1 < result2:
        return 1
    else:
        return 0


n = int(input())
group = [
    input() for _ in range(n)
]

group.sort(key = cmp_to_key(compare))
group = ''.join(group)
print(group)
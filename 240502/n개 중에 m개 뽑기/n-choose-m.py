N, M = tuple(map(int, input().split()))
ans = []


def print_all():
    for elem in ans :
        print(elem, end =' ')
    print()


def Choose(curr_num, value):
    global ans
    if curr_num == M:
        print_all()
        return

    for i in range(value, N + 1):
        ans.append(i)
        Choose(curr_num+1, i+1)
        ans.pop()

Choose(0, 1)
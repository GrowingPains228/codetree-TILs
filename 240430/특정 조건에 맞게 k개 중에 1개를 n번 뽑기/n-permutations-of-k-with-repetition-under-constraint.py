k,n = tuple(map(int, input().split()))
ans = []

def print_all():
    for elem in ans:
        print(elem, end = ' ')
    print()


def triple_same(num):
    return ans[-2] == ans[-1] == num


def choose(curr_num):
    if curr_num == n:
        print_all()
        return

    for i in range(1, k+1):
        if len(ans) < 2 or not triple_same(i):
            ans.append(i)
            choose(curr_num+1)
            ans.pop()


choose(0)
# 1~ n가지의 수
n = int(input())
visited = [False]*(n+1)
ans = []


def print_all():
    for elem in ans:
        print(elem, end = ' ')
    print()


def choose(curr_num):
    if curr_num == n+1:
        print_all()
        return

    for i in range(1,n+1):
        if visited[i]:
            continue

        visited[i] = True
        ans.append(i)
        choose(curr_num+1)
        visited[i] = False
        ans.pop()


choose(1)
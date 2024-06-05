d = dict()


def add(k, v):
    d[k] = v


def remove(k):
    d.pop(k)


def find(k):
    if k in d:
        return d[k]
    else:
        return None


n = int(input())
for _ in range(n):
    command = input().split()
    if command[0] == "add":
        add(command[1], command[2])
    elif command[0] == "find":
        print(find(command[1]))
    else:
        remove(command[1])
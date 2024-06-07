from sortedcontainers import SortedDict

n = int(input())
sd = SortedDict()

def add(k, v):
    sd[k] = v


def remove(k):
    sd.pop(k)


def find(k):
    if k in sd:
        return sd[k]
    else :
        return None


def print_list():
    if len(sd) == 0:
        print(None)
    else:
        for key, value in sd.items():
            print(value, end = " ")
        
        print()


for _ in range(n):
    command = input().split()

    if command[0] == "add":
        add(int(command[1]), int(command[2]))
    elif command[0] == "remove":
        remove(int(command[1]))
    elif command[0] == "find":
        v = find(int(command[1]))
        print(v)
    else :
        print_list()
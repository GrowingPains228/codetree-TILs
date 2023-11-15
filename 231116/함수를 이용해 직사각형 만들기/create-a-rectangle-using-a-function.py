n,m = tuple(map(int, input().split()))

def print_1(row, columns) :
    for _ in range(row) :
        print("1"*columns)

print_1(n,m)
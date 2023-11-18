N = int(input())

def start_print(n) :
    if n == 0 :
        return

    start_print(n-1)
    print("*"*n)

start_print(N)
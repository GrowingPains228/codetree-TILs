N = int(input())

def N_print(N) :
    if N == 0 :
        return

    N_print(N-1)
    print("HelloWorld")

N_print(N)
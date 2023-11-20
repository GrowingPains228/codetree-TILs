N = int(input())

def call_N(N) :
    if N == 1 :
        return 2
    elif N == 2 :
        return 4
    
    return (call_N(N-2) * call_N(N-1)) % 100

print(call_N(N))
N = int(input())

def sum_allSeat(N) :
    if N < 10 :
        return N**2
    
    return sum_allSeat(N//10) + (N%10)**2

print(sum_allSeat(N))
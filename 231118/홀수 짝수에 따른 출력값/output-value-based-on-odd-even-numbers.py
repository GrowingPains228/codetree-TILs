N = int(input())

def even_odd(n) :
    if n == 1 or n == 2:
        return n

    #짝수나 홀수나 2 씩 뺄셈을 하면서 내려가면 결국 1이나 2 를 만나게 된다.
    return even_odd(n-2) + n

print(even_odd(N))
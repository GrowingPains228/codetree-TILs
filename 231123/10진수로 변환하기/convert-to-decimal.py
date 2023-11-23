digits = list(input())
digits = map(int, digits)
n = 0

for digit in digits :
    n = n * 2 + digit

print(n)
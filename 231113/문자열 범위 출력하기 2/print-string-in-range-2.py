string = input()
n = int(input())

n = n if len(string) > n else len(string)

for elem in string[-1:-1-n:-1] :
    print(elem, end = "")
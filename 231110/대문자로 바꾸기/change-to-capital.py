arr = [list(map(ord,input().split())) for _ in range(5)]
a_int = ord('a')
for i in range(5) : 
    for j in range(3) : 
        arr[i][j] = arr[i][j] - a_int + ord('A')
        print(chr(arr[i][j]), end = " ")
    print()
n = int(input())
arr = list(map(int, input().split()))

max_number = -1

for i in range(n) :
    if max_number < arr[i] :
        cnt = 0

        for j in range(n) :
            if cnt > 1 :
                break

            if arr[i] == arr[j] :
                cnt += 1
            

        if cnt == 1 :
            max_number = arr[i]

print(max_number)
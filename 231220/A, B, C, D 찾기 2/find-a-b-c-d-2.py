import sys

arr = list(map(int, input().split()))
arr.sort()
MAX_NUM = max(arr)

for a in range(1, MAX_NUM + 1) :
    if arr[0] == a :
        for b in range(a, MAX_NUM + 1 - a) :
            if arr[1] == b :
                for c in range(b, MAX_NUM + 1 - a - b) :
                    for d in range(c, MAX_NUM + 1 - a - b - c) :
                        new_arr = [a,b,c,d,a+b,b+c,c+d,d+a,a+c,b+d,a+b+c,a+b+d,a+c+d,b+c+d,a+b+c+d]
                        new_arr.sort()

                        is_same = True
                        for num1, num2 in zip(new_arr, arr) :
                            if num1 != num2 :
                                is_same = False
                                break
                        
                        if is_same :
                            print(a,b,c,d)
                            sys.exit()
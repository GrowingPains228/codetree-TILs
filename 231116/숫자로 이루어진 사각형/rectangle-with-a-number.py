n = int(input())

def print_rectangle(num) :
    cnt = 1
    for _ in range(num) :
        for _ in range(num) :
            print(cnt, end = " ")
            cnt += 1
            if cnt > 9 :
                cnt = 1
        print()
        

print_rectangle(n)
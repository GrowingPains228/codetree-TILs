n = int(input())
string = input()

ans = 1
for i in range(1, n) :

    # 2번 이상 나오는지 판단하기 위한 bool 변수
    twice = False

    for j in range(n -i + 1) :
        for k in range(j+1, n -i + 1) :

            is_same = True
            for l in range(i):
                if string[j + l] != string[k + l] :
                    is_same = False
            
            if is_same :
                twice = True

    if twice :
        ans = i + 1
    else :
        break

print(ans)
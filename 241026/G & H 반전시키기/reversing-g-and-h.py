# 입력 받기
n = int(input())
initSting = input()
goalString = input()

ans = 0
IsCouning = False
for i in range(len(initSting)):
    if initSting[i] == goalString[i]:
        IsCouning = False
    else :
        if IsCouning:
            continue
        else:
            IsCouning = True
            ans += 1


print(ans)
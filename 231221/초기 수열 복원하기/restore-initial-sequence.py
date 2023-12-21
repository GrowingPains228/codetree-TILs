n = int(input())
arr = list(map(int, input().split()))
origin = [0] * n # 1이상의 숫자들로 세팅되어 있어야 하므로.

def sumulation(idx) :
    num1, num2 = origin[idx], arr[idx] - origin[idx]

    #동일한 숫자가 등장하면 
    if num2 in origin or num1 == num2 or num2 < 0:
        return False

    # 동일한 숫자들이 존재하지 않으면, 이곳으로 넘어간다.
    origin[idx+1] = num2
    if idx + 1 == n - 1 :
        return True

    return sumulation(idx+1)
            
# 처음 arr[0] 값에 따라서 분기가 나뉘므로, 처음 분기 들을 계산해준다.
num1, num2 = 0,0
for i in range(1, arr[0]) :
    #경우의 수 계산
    num1, num2 = i, arr[0]-i
    if num1 == num2:
        continue

    origin[0], origin[1] = num1, num2


    #시뮬레이션 실행
    #시물레이션 결과가 맞으면, 밖으로 빠져나와 origin을 출력
    if sumulation(1) :
        break
    # 결과가 맞지 않으면 맞을 때가지 다시 경우의 수 대입하여 실행.
    else :
        origin = [0] * n

for elem in origin :
    print(elem, end = ' ')
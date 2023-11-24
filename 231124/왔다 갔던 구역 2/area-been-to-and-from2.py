def move_set(x,char) :
    if char == "L" :
        return -1 * x
    else :
        return x

#입력 받기
n = int(input())

road = [0] * 100
current_idx = 0
#n번에 걸쳐서 입력 받기
for _ in range(n) :
    x,Ro = tuple(input().split())
    x = int(x)
    in_de = 1   # 증감 변수 정의

    # L 이라면 왼쪽으로 가야하므로, 이에대한 Offest 업데이트
    if Ro == "L" :
        x *= -1
        in_de = -1

    # 종료될 인덱스 저장
    end_idx = current_idx + x

    # 지나간 경로 연산
    for i in range(current_idx, end_idx , in_de) :
        road[i] += 1

    # 현재 인덱스 저장
    current_idx = end_idx + 1 if end_idx >= current_idx else 0

count = 0
for elem in road :
    if elem >= 2 :
        count += 1

print(count)
#입력 받기
n = int(input())
road = [0] * 100
current_idx = 0
collect_arr = []

#n번에 걸쳐서 입력 받기
for _ in range(n) :
    x,Ro = tuple(input().split())
    x = int(x)
    in_de = 1   # for문내 증감 변수 정의
    start_tf = 0
    end_tf = 0

    # L 이라면 왼쪽으로 가야하므로, 이에대한 Offest 업데이트
    # 오른 쪽으로 갈때는 원래 알고리즘 대로 하면 되지만,
    # 왼쪽으로 이동할때는 약간의 Offset을 주어 각 끝점에 유의 하여야한다.
    if Ro == "L" :
        start_tf -= 1
        x *= -1 # 방향
        in_de = -1
        end_tf = -1

    # 종료될 인덱스 저장
    end_idx = current_idx + x

    # 지나간 경로 연산
    for i in range(current_idx + start_tf, end_idx + end_tf, in_de) :
        road[i] += 1

    # 현재 인덱스 저장
    current_idx = end_idx

count = 0
for elem in road :
    if elem >= 2 :
        count += 1

print(count)
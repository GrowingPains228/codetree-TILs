# 입력
# n : 턴의 수/ m : 윳놀이 판의 상태 / k : 말의 수
n, m, k = tuple(map(int, input().split()))
move_arr = list(map(int, input().split()))
player_state_Array = [0]*k # 현재 말이 어디 인덱스에 존재하는지 업데이트
ans = 0

def Cal_Score():
    score = 0
    for player_pos in player_state_Array:
        if player_pos >= m-1:
            score +=1
    return score


# 턴의 수를 입력으로 받는다.
def choose(curr_num):
    global ans
    if curr_num == n:
        ans = max(ans, Cal_Score())
        return

    for i in range(k):
        # 조건 : 플레이어가 마지막 구간에 도착하지 않았을 때만 선택
        if player_state_Array[i] < m-1:
            score = move_arr.pop()
            player_state_Array[i] += score
            choose(curr_num+1)
            move_arr.append(score)
            player_state_Array[i] -= score


choose(0)
print(ans)
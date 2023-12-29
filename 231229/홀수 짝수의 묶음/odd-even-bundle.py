n = int(input())
arr = list(map(int, input().split()))

# 짝 수 개수와 홀 수 개수를 파악해서, 일정하게 묶어주면 관리하기 편할 것 같다.
# 짝 + 홀 = 홀, 홀 + 홀 = 짝, 홀 + 홀 + 홀 = 홀 ...
# 짝, 홀, 짝, 홀 ... 이런식으로 나와야 하므로, 짝수와 홀수를 적절하게 조합하는게 핵심!
cnt_even = 0
cnt_odd = 0

# 1. 홀수, 짝수 의 개수를 구하자.
for elem in arr :
    if elem % 2 == 0 :
        cnt_even += 1
    else : 
        cnt_odd += 1

# 2. 짝수 만들기 = 홀수를 짝수개로 조합 , 짝수 n개 조합
#    홀수 만들기 = 홀수 n개 조합, 짝수 조합에 홀수의 홀수개 조합
cnt = 0
is_even = True # True : 짝수, False : 홀수
while cnt_even > 0 or cnt_odd > 0 :
    if is_even :
        # 짝수가 있다면 짝수 1개 사용하기
        if cnt_even > 0 :
            cnt_even -= 1
        # 짝수가 없다면 홀수 2개 사용해야하는데, 
        else:
            # 2개가 없다면, 이전 홀 수 만드는 시점에서 3개로 만들어 주면서 게임 끝내야함.
            if cnt_odd < 2:
                cnt -= 1
                break

            cnt_odd -= 2
    else :
        # 홀수가 없다면, 짝수로 홀수를 만들 수 있는 방법이 없으므로, 끝내기
        if cnt_odd == 0 :
            break

        # 홀수가 있다면 홀수 사용하기
        cnt_odd -= 1
    
    cnt += 1
    is_even = not is_even

print(cnt)
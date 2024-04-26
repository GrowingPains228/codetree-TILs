n = int(input())
cnt_anwser = 0
answer = []

def Is_butiful_num():
    target = answer[0]
    cnt = 1
    for i in range(1, n):
        if target == answer[i]:
            cnt += 1
        else:
            if cnt % target != 0:
                return False

            target = answer[i]
            cnt = 1

    if cnt % target  == 0:
        return True

    return False


def choose(num):
    global cnt_anwser, answer
    if num == n+1:
        if Is_butiful_num():
            cnt_anwser += 1
        return
    
    for i in range(1, 5):
        answer.append(i)
        choose(num+1)
        answer.pop()


choose(1)
print(cnt_anwser)
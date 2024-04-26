n = int(input())
cnt_anwser = 0
answer = []
index_cnt = [0] * 5

def Is_butiful_num():
    tf = False
    elem = answer[0]
    elem_cnt = 1
    curr_idx = 0
    while curr_idx < n :
        if curr_idx == n-1 or elem != answer[curr_idx]:
            if elem_cnt % elem == 0:
                tf = True
                break
            else:
                elem = answer[curr_idx]
                elem_cnt = 1
        else :
            elem_cnt += 1
    
        curr_idx += 1
    return tf


def choose(num):
    global cnt_anwser
    if num == n:
        if Is_butiful_num():
            cnt_anwser += 1
        return
    
    for i in range(1, 5):
        answer.append(i)
        choose(num+1)
        answer.pop()


choose(0)
print(cnt_anwser)
str_arr = input()
str_length = len(str_arr)

def Encoding() :
    global str_arr
    temp_arr = ''
    idx = 0
    while idx < len(str_arr):
        cnt = count_strcnt(idx, str_arr[idx])
        temp_arr += (str_arr[idx] + str(cnt))
        idx += cnt
    return len(temp_arr)
        

# 중복된 문자 계산해서 갯수 리턴하는 함수
def count_strcnt(start_Idx, char) :
    global str_arr
    curIdx = start_Idx
    cnt = 1
    while curIdx < str_length - 1:
        if str_arr[curIdx + 1] != str_arr[curIdx]:
            break

        cnt += 1
        curIdx += 1
        
    return cnt


def shift():
    global str_arr
    str_arr = list(str_arr)
    temp = str_arr[str_length-1]
    for i in range(str_length-1, 0, -1) :
        str_arr[i] = str_arr[i-1]
    str_arr[0] = temp


ans = str_length * 2
for _ in range(str_length-1):
    shift()
    ans = min(ans, Encoding())

print(ans)
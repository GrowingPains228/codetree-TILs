M,D = tuple(map(int, input().split()))

def return_MaxDays_about_Month(month) :
    #일단 12월 넘는 수가 입력된건 아닌지 체크
    if month > 12 :
        return -1

    if month == 2 :
        return 28

    # 7월 이전은 홀수 달이 31, 짝수 달이 30
    if month <= 7 :
        if month%2 == 1 :
            return 31
        else :
            return 30
    else :     # 7월 이후에 홀수 달이 30, 짝수 달이 31
        if month%2 == 1 :
            return 30
        else :
            return 31

#최종 체크 함수
def CheckDays(month, day) :
    max_days = return_MaxDays_about_Month(month)
    if max_days < 0 :
        return False
    else :
        if day > max_days :
            return False
        else :
            return True

print("Yes" if CheckDays(M,D) else "No")
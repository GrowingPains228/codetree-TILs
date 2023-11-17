Y, M, D = tuple(map(int, input().split()))

# 1. 윤년 판별 함수
def is_leap(Y) :
    if Y % 4 != 0 :
        return False
    
    #여기 까지 왔다는건, '4의 배수'
    #이때, 100의 배수가 아니라면 확실히 윤년!
    if Y % 100 != 0 :
        return True
    
    #여기 까지 왔다는건, '100의 배수'
    #그 중 400의 배수라면 확실히 윤년
    if Y % 400 == 0 :
        return True

    #위에 모두 해당사항이 없으므로, 윤년 아님
    return False

# 달(month)에 따른 최대 일 수
def check_MaxDay_About_Month(isLeap, M) :
    if M == 2 :
        if isLeap :
            return 29
        else :
            return 28

    if M in (4, 6, 9, 11) :
        return 30
    else :
        return 31

# 달(month)에 따른 계절
def what_season(M) :
    if M >= 3 and M <= 5 :
        print("Spring")
    elif M >= 6 and M <= 8 :
        print("Summer")
    elif M >= 9 and M <= 11 :
        print("Fall")
    else : 
        print("Winter")
    
#최종 함수
def check_month(Y, M, D) : 

    max_days = check_MaxDay_About_Month(is_leap(Y), M)
    # 일수가 범위안에 들어오는 달인지 체크
    if max_days < D :
        print(-1)

    #들어왔다면 이제 계절 판별해서 출력
    what_season(M)

check_month(Y,M,D)
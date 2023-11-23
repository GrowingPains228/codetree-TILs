# 무슨 요일인지는 쉽다. 7로 나눈 나머지를 기준으로 계산하면 쉽다.
month_to_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week_type_arr = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
m1, d1, m2,d2 = tuple(map(int, input().split()))

def cal_days(m, d) :
    days = 0
    for month in range(1,m) :
        days += month_to_days[month]

    return days + d

total_days = cal_days(m2, d2) - cal_days(m1, d1)
print(week_type_arr[(total_days)%7])
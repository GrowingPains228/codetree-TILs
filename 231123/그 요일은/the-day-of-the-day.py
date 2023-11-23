month_to_days = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week_type_arr = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

m1, d1, m2, d2 = tuple(map(int, input().split()))
day_of_the_week = input()

def cal_days(m, d) :
    days = 0
    for i in range(1, m) :
        days += month_to_days[i]
    
    days += d
    return days

# 총 일 수 를 구해서
total_days = cal_days(m2, d2) - cal_days(m1, d1)
# 입력된 요일의 인덱스를 찾는다
idx = week_type_arr.index(day_of_the_week)

#총 몇번 등장하는지는 몫을 구하면 된다.
count = total_days//7 + ( 1 if total_days%7 >= idx else 0)

print(count)
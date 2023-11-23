month_to_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def cal_minute(day, hour, minute) :
    return day*24*60 + hour*60 + minute

a,b,c = tuple(map(int, input().split()))

minutes = cal_minute(a,b,c)-cal_minute(11,11,11)
if minutes < 0 :
    print(-1)
else :
    print(minutes)
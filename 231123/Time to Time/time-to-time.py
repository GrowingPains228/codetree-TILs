a,b,c,d = tuple(map(int, input().split()))

def cal_min(hour, minute) :
    return hour * 60 + minute

time2 = cal_min(c,d)
time1 = cal_min(a,b)

print(time2-time1)
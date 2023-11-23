m1, d1, m2, d2 = tuple(map(int, input().split()))

#                  1.  2.  3.  4.  5.  6.  7.  8.  9. 10. 11. 12.
num_of_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def cal_days(m1, d1, m2, d2) :
    days = 0
    for month in range(m1, m2) :
        days += num_of_days[month]
    days += -d1 + 1
    days += d2

    return days

print(cal_days(m1, d1, m2, d2))
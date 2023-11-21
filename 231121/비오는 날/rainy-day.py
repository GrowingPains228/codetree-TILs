class WeatherInfo :
    def __init__ (self, day_Week, date, info) :
        self.day_Week = day_Week
        self.date = date
        self.info = info

n = int(input())

arr = [ tuple(input().split()) for _ in range(n)]

# 비 오는날만 골라서 담자.
info_arr = [
    WeatherInfo(day_Week, date, info) for date, day_Week, info in arr if info == "Rain"
]


last_rain_info = info_arr[0]
for i in range(1,len(info_arr)) :
    if last_rain_info.date > info_arr[i].date :
        last_rain_info = info_arr[i]

print(last_rain_info.date, last_rain_info.day_Week, last_rain_info.info)
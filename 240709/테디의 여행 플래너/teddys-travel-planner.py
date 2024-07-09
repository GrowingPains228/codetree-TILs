class City:
    def __init__(self, name):
        self.name = name
        self.right = None
        self.left = None


def connect(a, b):
    if a is not None:
        a.right = b
    if b is not None:
        b.left = a


class Pin:
    def __init__(self, city):
        self.curCity = city


    def MoveRight(self):
        next_city = self.curCity.right
        if next_city is None:
            return

        self.curCity = next_city;


    def MoveLeft(self):
        next_city = self.curCity.left
        if next_city is None:
            return
            
        self.curCity = next_city;


    def PushRight(self, city):
        newCity = city

        if self.curCity is None:
            self.curCity = newCity
            return
        
        cityR = self.curCity.right
        connect(self.curCity, newCity)
        if cityR is None:
            return
        connect(newCity, cityR)


    def removRight(self):
        cityR = self.curCity.right
        if cityR is None:
            return
        
        connect(self.curCity, cityR.right)
        cityR.right = cityR.left = None


n, q = tuple(map(int, input().split()))
cityList = list(input().split())
cityArray = [ None ] * n
for i in range(n):
    cityArray[i] = City(cityList[i])

pin = Pin(cityArray[0])
for i in range(1, n):
    connect(cityArray[i-1], cityArray[i])

connect(cityArray[n-1], cityArray[0])

for _ in range(q):
    cmd = input().split()
    if cmd[0] == '1':
        pin.MoveRight()
    elif cmd[0] == '2':
        pin.MoveLeft()
    elif cmd[0] == '3':
        pin.removRight()
    else:
        pin.PushRight(City(cmd[1]))

    curPin = pin.curCity
    city1, city2 = curPin.left, curPin.right
    if city1 == city2 or (city1 is None and city2 is None):
        print(-1)
    else:
        print(city1.name, city2.name)
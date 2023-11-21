class spt :
    def __init__(self, secretCode, place, time) :
        self.secretCode = secretCode
        self.place = place
        self.time = time


s,p,c = tuple(input().split())

exClass = spt(s, p, c) 
print(f"secret code : {exClass.secretCode}")
print(f"meeting point : {exClass.place}")
print(f"time : {exClass.time}")
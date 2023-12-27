x = int(input())
t = 0
left_dist = x
v = 1

while True:
    left_dist -= v
    t += 1

    if left_dist == 0:
        break
    
    if left_dist >= (v + 1) * (v + 2) / 2:
        v += 1
    elif left_dist >= v * (v + 1) / 2:
        pass
    else :
        v -= 1
    
print(t)
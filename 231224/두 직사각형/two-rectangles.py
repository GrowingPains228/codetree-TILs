x1, y1, x2, y2 = tuple(map(int, input().split()))
a1, b1, a2, b2 = tuple(map(int, input().split()))

def is_include() :
    if x1 > a2 or x2 < a1 or y1 > b2 or y2 < b1 :
        return False
    return True

if is_include() :
    print("overlapping")
else :
    print("nonoverlapping")
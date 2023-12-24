x1,x2,x3,x4 = tuple(map(int, input().split()))

def is_include() :
    if x2 < x3 or x1 > x4 :
        return False
    
    return True

if is_include() :
    print("intersecting")
else :
    print("nonintersecting")
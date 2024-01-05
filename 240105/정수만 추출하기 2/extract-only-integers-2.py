a,b = tuple(input().split())

def is_str(elem) :
    order = ord(elem)
    if order >= ord('a') and order <= ord('z') :
        return True
    
    if order >= ord('A') and order <= ord('Z') :
        return True
    
    return False

new_a = ""
for i in range(len(a)) :
    if is_str(a[i]) :
        continue
    
    new_a += a[i]

new_b = ""
for i in range(len(b)) :
    if is_str(b[i]) :
        continue
    
    new_b += b[i]

print(int(new_a) + int(new_b))
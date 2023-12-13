n, b = tuple(map(int, input().split()))

p = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

p.sort(key = lambda x : (x[0]+ x[1]))

ans = 0
for i in range(n) :
    order = 0
    price = 0
    for j in range(n) :
        gift, trans = p[j]

        if i == j :
            gift //= 2
        
        if price + (gift + trans) <= b :
            price += (gift + trans)
            order += 1
    
    ans = max(ans, order)

print(ans)
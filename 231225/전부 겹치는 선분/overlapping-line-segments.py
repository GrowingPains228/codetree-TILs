MAX_RANGE = 100
n = int(input())


lines = [
    tuple(map(int, input().split()))
    for _ in range(n)
]

count_lines = [0]*(MAX_RANGE+1)

#이거 전체를 전부 +=1 해주면 되지 않나..?
for (x1,x2) in lines :
    for i in range(x1, x2+1) :
        count_lines[i] += 1
    
if n in count_lines :
    print("Yes")
else :
    print("No")
#수열 A의 개수와 수열 B의 개수
n1, n2 = tuple(map(int, input().split()))

# 수열 A,B를 받아온다.
A = list(map(int, input().split()))
B = list(map(int, input().split()))

#연속 수열 판별 함수
def is_continuous(parent, child) :
    for i in range(0, len(parent) - len(child) + 1) :
        if parent[i] == child[0] :
            for j in range(1, len(child) ) :
                if parent[i + j] != child[j] :
                    break
                
                if j == len(child) - 1 :
                    return True
        
    return False


print("Yes" if is_continuous(A,B) else "No")